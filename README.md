# Overseer
A server control hub application.

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
