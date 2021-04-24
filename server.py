#!/bin/python
import yaml, requests, datetime
from flask import Flask, request
import databaseHandler

with open("config.yaml") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

app = Flask(__name__)
dbh = databaseHandler.DatabaseHandler(config['databaseAddress'])

@app.route('/api/config/<serverID>', methods=['GET','PUT'])
def remoteConfig(serverID):
    if request.method == 'GET':
        addr = dbh.serverFromID(serverID)['serverAddr']
        res = requests.get(f"http://{addr}/config")
        return res.json() 
    elif request.method == 'PUT':
        data = request.get_json()
        addr = dbh.serverFromID(serverID)['serverAddr']
        print(data)
        res = requests.put(f"http://{addr}/config",json = data)
        return res.json()

@app.route('/api/config/servers/<serverID>', methods=['GET'])
def getServerConf(serverID):
    res = dbh.serverFromID(serverID)
    res.pop('_id')
    return res

@app.route('/api/config/servers',methods=['GET', 'POST'])
def configServers():
    if request.method == 'GET':
        return dbh.getServers()
    elif request.method == 'POST':
        data = request.get_json()
        dbh.addServer(data)
        return {'success':True}

@app.route('/api/config/servers/<serverID>', methods=['PUT', 'DELETE'])
def editServerConfig(serverID):
    if request.method == 'PUT':
        data = request.get_json()
        dbh.editServer(data,serverID)
        return {'success':True}
    elif request.method == 'DELETE':
        dbh.removeServer(serverID)
        return {'success':True}

@app.route('/api/backups/start', methods=['POST'])
def startBackup():
    master = dbh.getMaster()
    slaves = dbh.getSlaves()
    servers = dbh.getServers()['servers']
    dateCode = int(datetime.datetime.now().strftime('%Y%m%d') + '01')
    
    backupServers(servers, dateCode)
    syncToMaster(servers, master)
    syncMasterToSlaves(slaves, master)
    return {
            "success":True,
            "dateCode":dateCode
            }

@app.route('/api/backups/purge', methods=['DELETE'])
def purgeBackup():
    servers = dbh.getServers()['servers']
    dateCode = int(request.get_json()['dateCode'])
    data = {"date":dateCode}
    for server in servers:
        addr = dbh.serverFromID(server)['serverAddr']
        requests.post(f"http://{addr}/backup/purge", json = data)
    return {'success':True}

@app.route('/api/backups/usage/<serverID>', methods = ['GET'])
def getUsage(serverID):
    addr = dbh.serverFromID(serverID)['serverAddr']
    res = requests.get(f"http://{addr}/backup/usage")
    return res.json()

def backupServers(servers, dateCode):
    for server in servers:
        addr = dbh.serverFromID(server)["serverAddr"]
        data = {"uid":dateCode}
        requests.post(f"http://{addr}/backup/start", json = data)

def syncToMaster(servers, master):
    masterAddr = master['serverAddr']
    backupsDir = requests.get(f"http://{masterAddr}/backup/parent").json()['parentDir']
    masterAddr = masterAddr[:-5]
    destination = f"overseer@{masterAddr}:{backupsDir}"
    data = {"dest":destination}
    for server in servers:
        addr = dbh.serverFromID(server)['serverAddr']
        requests.post(f"http://{addr}/backup/sync", json = data)

def syncMasterToSlaves(slaves,master):
    masterAddr = master['serverAddr']
    for slave in slaves:
        addr = slave['serverAddr']
        backupsDir = requests.get(f"http://{addr}/backup/parent").json()['parentDir']
        addr = addr[:-5]
        destination = f"overseer@{addr}:{backupsDir}"
        data = {"dest":destination}
        print(data)
        requests.post(f"http://{masterAddr}/backup/sync", json = data)
