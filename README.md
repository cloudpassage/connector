# Halo Event Connector v1.10

[![Build Status](https://travis-ci.org/cloudpassage/connector.svg?branch=master)](https://travis-ci.org/cloudpassage/connector)
[![Maintainability](https://api.codeclimate.com/v1/badges/0ba702a4cf12a6025067/maintainability)](https://codeclimate.com/github/cloudpassage/connector/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/0ba702a4cf12a6025067/test_coverage)](https://codeclimate.com/github/cloudpassage/connector/test_coverage)

### Requirements

This tool requires the following Python packages:
* cloudpassage
* python-dateutil
* pytz

Install the requirements the easy way with `pip install -r requirements.txt`

### Intro - Quick Start

While this tool can be run by a variety of different scheduling mechanisms, the
most common pattern is to use cron.

In this example:
* We will use cron to run the event connector.
* The event connector will append Halo events to a file in key-value format.
(in this example, `/var/log/halo-kv.log`)
* In this scenario, we need to retrieve events starting on July 1st, 2017 (Halo
   only retains events for 90 days, so this date is just used as an example).

First, we check out this repository in `/opt/cloudpassage/`:

* `mkdir -p /opt/cloudpassage`
* `cd /opt/cloudpassage`
* `git clone https://github.com/cloudpassage/connector`

Next, configure Halo authentication information for the connector:

* In your CloudPassage portal account, generate an auditor (read-only) API key.
* Place the API key and secret, pipe-separated, in a file at
`/opt/cloudpassage/connector/config/halo.auth`.  The file will contain one
line, which looks like this: `haloapikey|haloapisecret`, replacing `haloapikey`
with the key ID for your Halo API key, and replacing `haloapisecret` with your
API key's secret.

Next, configure cron to run the Halo connector every 5 minutes:

* Run `crontab -e`
* Add a line with the desired schedule:

```
*/5 * * * * /opt/cloudpassage/connector/halo_events.py --starting=2017-07-01 --auth=/opt/cloudpassage/connector/config/halo.auth --configdir=/opt/cloudpassage/config --kvfile=/var/log/halo-kv.log >/dev/null 2>&1
```

Save and exit crontab.

Monitor the `/var/log/halo-kv.log` file to see events from your Halo account.


### Implementation Notes

__Multiple accounts:__

If you are extracting events from more than one (supports up to 5) Halo
accounts, you can specify those in your halo.auth file like this:

```
key_id_1|secret_1
key_id_2|secret_2
...
...
key_id_5|secret_5
```

__CLI Options:__
```
usage: halo_events.py [-h] [--starting STARTING] --auth AUTH
                     [--threads THREADS] [--batchsize BATCHSIZE]
                     [--configdir CONFIGDIR] [--jsonfile JSONFILE]
                     [--ceffile CEFFILE] [--leeffile LEEFFILE]
                     [--kvfile KVFILE] [--facility FACILITY] [--cef] [--kv]
                     [--leefsyslog] [--cefsyslog] [--kvsyslog] [--sumologic]

Event Connector

optional arguments:
  -h, --help            show this help message and exit
  --starting STARTING   Specify start of event time range in ISO-8601 format
  --auth AUTH           Specify a file containing CloudPassage Halo API keys -
                        Key ID and Key secret pairs (up to 5)
  --threads THREADS     Start num threads each reading pages of events in
                        parallel
  --batchsize BATCHSIZE
                        Specify a limit for page numbers, after which we use
                        since
  --configdir CONFIGDIR
                        Specify directory for configration files (saved
                        timestamps)
  --jsonfile JSONFILE   Write events in raw JSON format to file with given
                        filename
  --ceffile CEFFILE     Write events in CEF (ArcSight) format to file with
                        given filename
  --leeffile LEEFFILE   Write events in LEEF (QRadar) format to file with
                        given filename
  --kvfile KVFILE       Write events as key/value pairs to file with given
                        filename
  --facility FACILITY   --facility=<faility,priority> Facility options:auth
                        authpriv cron daemon kern local0 local1 local2local3
                        local4 local5 local6 local7 lpr mail news sysloguser
                        uucp Priority options: alert crit debug emerg errinfo
                        notice warning [default: user,info]
  --cef                 Write events in CEF (ArcSight) format to standard
                        output (terminal)
  --kv                  Write events as key/value pairs to standard output
                        (terminal)
  --leefsyslog          Write events in LEEF (QRadar) format to syslog server
  --cefsyslog           Write events in CEF (ArcSight) format to syslog server
  --kvsyslog            Write events as key/value pairs to local syslog daemon
  --sumologic           Send events (JSON) format to Sumologic. Must specify sumologic_https_url in configs/portal.yml
```

### Halo Event Connector on Linux

* Install Python 2.7.11 or newer (https://www.python.org/downloads)

* Once Python is installed, install the necessary Python modules:

```
pip install -r requirements.txt
```


* Download the Halo Event Connector (https://github.com/cloudpassage/connector)

6. Create the `halo.auth` file

7. Run the connector (must specify a starting cli parameter)

```
python halo_events.py --auth=halo.auth --starting=YYYY-MM-DD
```

### Halo Event Connector on Windows

* Install Python 2.7.11 or newer (https://www.python.org/downloads/windows/)

* Add python installation folder to system PATH environmental variable or
create PYTHONPATH environment variable and set installation folder location as
follows (C:\Python27\lib;C:\Python27)

* Once Python is installed, install the necessary Python modules

```
python -m pip install -r requirements.txt
```

* Download the Halo Event Connector (https://github.com/cloudpassage/connector)

* Create the halo.auth file

* Run the connector (currently must specify a starting cli parameter)

```
python halo_events.py --auth=halo.auth --starting=YYYY-MM-DD
```

#### Remote Syslog Windows
* Navigate to `configs/portal.yml` you can specify the syslog host there via

  windows_syslog_host:
  windows_syslog_port:


#### Testing
Requirements:
  * Docker engine
  * A Halo account with events generated in the last 24 hours
Testing:
  * Clone this repository
  * Navigate to the root directory of this repository
  * Set the following environment variables:
    * HALO_API_KEY
    * HALO_API_SECRET_KEY
  * Run the following command:

  ```
  docker build \
      --build-arg HALO_API_KEY=$HALO_API_KEY \
      --build-arg HALO_API_SECRET_KEY=$HALO_API_SECRET_KEY \
      .
  ```

All testing happens in the first stage of the container build.


<!---
#CPTAGS:community-supported integration archive
#TBICON:images/python_icon.png
-->
