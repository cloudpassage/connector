Changelog
=========

v1.10
-----

Changes
~~~~~~~

- Undefined CEF events get event ID 999. [Ash Wilson]

- Added CloudSecure events. [Ash Wilson]

  Alignment of tests

  Closes #18

Fix
~~~

- Python process spawning per write. [Jye Lee]

Other
~~~~~

- Per HP, remove escape_specials. [Jye Lee]

- Add destinationTranslatedAddress to server_ip_address for cef. [Jye
  Lee]

- Add new event types to cef. [Jye Lee]

- Add cef event: portal_audit_policy_modified. [Jye Lee]

- Cef field changes per certification recommendation. [Jye Lee]

- Allow custom cef mapping and labelling for cs fields. [Jye Lee]

- Update cef.yml with container events. [Jye Lee]

- Update readme with pip install pyopenssl. [eatwithforks]

- Update readme.md. [eatwithforks]

- Format json for sumo. [Jye Lee]

- Fix global var, use self. [Jye Lee]

- Forward events to sumologic. [Jye Lee]

- Improvement: dont paginate if data is empty. [Jye Lee]

- Add R41 events. [Jye Lee]

- Removed name: fname. [Hana Lee]

- Update cef.py. [Jye Lee]

- Escape special characters, capitalize cs1Label. [Jye Lee]

- \n between formatted_events. [Jye Lee]

- Utc format fix. [Jye Lee]

- Remove known events. [Jye Lee]

- Add event type exists test. [Jye Lee]

- Added new events to cef and leef. [Hana Lee]

- Update README.md. [mong2]

v1.9 (2017-04-24)
-----------------

- Update README. [Hana Lee]

- Update readme with contact and license information. [eatwithforks]

- Convert datetime in cef to match Archsight format. [Hana Lee]

- Add newline for test unit halo. [Jye Lee]

- Add newline for __init__ and config_helper. [Jye Lee]

- Remove comments. [Jye Lee]

- Added integration_string and unit test. [Jye Lee]

v1.8 (2016-12-08)
-----------------

- Upload v1.8 No 5k daily event limit restriction. [Jye Lee]

v1.7 (2015-10-28)
-----------------

- Expanded event ID and type mapping. [Ash Wilson]

- Corrected COPY syntax. [Ash Wilson]

- Corrected path for assets, automatically show README on start. [Ash
  Wilson]

- Adding Dockerfile. [Ash Wilson]

- Updated README w/ Dockerfile info. [Ash Wilson]

- Adding docs from old version of connector. [Ash Wilson]

- Created README.md. [Ash Wilson]

- Added support for Halo events created since last update. [Apurva
  Singh]

- Fix for deep pagination issues in ES. [Apurva Singh]

- Fixed typo. [Apurva Singh]

- Breaking the deep pagination cycle. [Apurva Singh]

- Added more input validations. [Apurva Singh]

- Adding code to handle precision level of milliseconds, as opposed to
  microseconds, in the event timestamps. [Apurva Singh]

- The conversion of timestamps from Halo to LEEF format wasn't working
  due to unexpected string lengths. This should handle any number of
  fractional second digits (from 3 to 6). [Apurva Singh]

- Added multithreaded execution support. Added support for retries on
  server failure. [Apurva Singh]

- Fixed issue with reauthentication when toekn expires. [Apurva Singh]

- Added support for logging to remote syslog server, when running
  haloEvents.py on Windows. [Apurva Singh]

- Added the required libraries for the Halo Event Connector. [Apurva
  Singh]

- Fixed a bug with how checkpoiting was being handled for events.
  [Apurva Singh]

- Create cpsyslog.py. [apurvasingh]

- Create haloEvents.py. [apurvasingh]

- Create .gitignore. [apurvasingh]


