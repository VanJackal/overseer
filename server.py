#!/bin/python
import yaml
from flask import Flask, request

with open("config.yaml") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

app = Flask(__name__)

@app.route('/api/config/<serverID>', methods=['GET','PUT'])
def remoteConfig(serverID):
    if request.method == 'GET':
        pass
    elif request.method == 'PUT':
        pass
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
        pass
    elif request.method == 'POST':
        pass
    return '<p>not yet implemented</p>'

@app.route('/api/backups/start', methods=['POST'])
def startBackup():
    return '<p>not yet implemented</p>'

@app.route('/api/backups/purge', methods=['POST'])
def purgeBackup():
    return '<p>not yet implemented</p>'
