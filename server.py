#!/bin/python
import yaml, requests
from flask import Flask, request
import databaseHandler

with open("config.yaml") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

app = Flask(__name__)
dbh = databaseHandler.DatabaseHandler(config['databaseAddress'])

@app.route('/api/config/<serverID>', methods=['GET','PUT'])
def remoteConfig(serverID):
    if request.method == 'GET':
        addr = dbh.serverFromID(serverID)
        res = requests.get(f"http://{addr}/config")
        return res.json() 
    elif request.method == 'PUT':
        data = request.get_json()
        addr = dbh.serverFromID(serverID)
        print(data)
        res = requests.put(f"http://{addr}/config",json = data)
        return res.json()
    return '<p>not yet implemented</p>'

@app.route('/api/config', methods=['GET','PUT'])
def localConfig():
    if request.method == 'GET':
        pass
    elif request.method == 'PUT':
        pass
    return '<p>not yet implemented</p>'

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
    return '<p>not yet implemented</p>'

@app.route('/api/backups/purge', methods=['POST'])
def purgeBackup():
    return '<p>not yet implemented</p>'
