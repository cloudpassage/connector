### First stage tests the code
FROM halotools/python-sdk:ubuntu-16.04_sdk-1.0.1 as TESTER

ENV PORTAL_YAML=/source/configs/portal.yml
ENV AUTH_FILE=/source/configs/keys.auth

ARG HALO_API_KEY
ARG HALO_API_SECRET_KEY

COPY ./ /source/

WORKDIR /source/

RUN pip install -r requirements-testing.txt

# Place creds for testing...
RUN echo "key_id: ${HALO_API_KEY}" >> ${PORTAL_YAML}
RUN echo "secret_key: ${HALO_API_SECRET_KEY}" >> ${PORTAL_YAML}
RUN echo "${HALO_API_KEY}|${HALO_API_SECRET_KEY}" > ${AUTH_FILE}

RUN py.test -vv --cov=lib /source/tests/

##########
###Second stage builds the container

FROM halotools/python-sdk:ubuntu-16.04_sdk-1.0.1
MAINTAINER toolbox@cloudpassage.com

COPY ./ /source/

WORKDIR /source/

RUN pip install -r requirements.txt
