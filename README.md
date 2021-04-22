# Overseer
A server control hub application.

-----

# API Documentation
*Still WIP*

## /api/config/{serverID} GET/PUT
`serverId` is the unique identifier for the server whose configs you want to access (typicaly the hostname of the server).

Method|Result
------|------
GET|Gets the config of the server identified by serverID
PUT|Sets the config of the server identified by serverID

## /api/config GET/PUT
Gets or sets the config for the control server

## /api/config/servers GET/POST

METHOD|RESULT
------|------
GET|Gets a list of all the servers being controlled by the overseer.
POST|Adds a server to the list of controlled servers

## /api/backups/start POST
Executes a backup and sync operation.

## /api/backups/purge POST
Purges all backups older than a given date.

Field|Type|Description
-----|----|-----------
dateCode|integer|Date code of form YYYYMMDD

## /api/backups/usage/{serverID} GET
Gets the current disk usage on the server identified by `serverID`

-----

# TODO / Feature List

## Frontend Control (React.js)
- [ ] Set configs
  - [ ] Server Specific
  - [ ] Global settings
  - [ ] manual config refresh from db
- [ ] Activate manual backup
- [ ] Check when last backup was done
- [ ] Check current backup size
- [ ] Check Remaining disk space per server

## Backend API (Flask.py)
- [ ] Actually sets the configs
- [ ] recieves requests from any control client
- [ ] saves data/records to database
- [ ] saves configs to database for ease of viewing

## Passive Control (Python)
- Activated by a Daemon/Task Schedular
- tells the api to initiate automated backups and updates
- api defines configuration

## Remote Client (Python)
*In seperate repo*
- [X] has configs to tell it what to backup to a backups directory
- [ ] should have install script
- [X] waits for packet telling it to initiate a backup or system update
- [X] reports backup dir size and disk usage
