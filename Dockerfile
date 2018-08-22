### First stage tests the code
FROM halotools/python-sdk:ubuntu-16.04_sdk-1.0.1 as TESTER

ENV PORTAL_YAML=/source/configs/portal.yml
ENV AUTH_FILE=/source/configs/keys.auth

ARG HALO_API_KEY
ARG HALO_API_SECRET_KEY
ARG CC_TEST_REPORTER_ID

RUN apt-get update && apt-get install -y git curl

COPY ./ /source/

WORKDIR /source/

RUN pip install -r requirements-testing.txt

# Place creds for testing...
RUN echo "key_id: ${HALO_API_KEY}" >> ${PORTAL_YAML}
RUN echo "secret_key: ${HALO_API_SECRET_KEY}" >> ${PORTAL_YAML}
RUN echo "${HALO_API_KEY}|${HALO_API_SECRET_KEY}" > ${AUTH_FILE}

# Set up code coverage tool
RUN curl -L https://codeclimate.com/downloads/test-reporter/test-reporter-latest-linux-amd64 > ./cc-test-reporter
RUN chmod +x ./cc-test-reporter
RUN ./cc-test-reporter before-build || echo "Not sending test results."

RUN py.test -vv --cov-report term-missing --cov-report xml --cov=lib /source/tests/; ./cc-test-reporter after-build -t coverage.py --exit-code $? || echo "Not sending test results."

##########
###Second stage builds the container

FROM halotools/python-sdk:ubuntu-16.04_sdk-1.0.1
MAINTAINER toolbox@cloudpassage.com

COPY ./ /source/

WORKDIR /source/

RUN pip install -r requirements.txt
