import pymongo

class DatabaseHandler:
    def __init__(self,dbAddr):
        dbClient = pymongo.MongoClient(f"mongodb://{dbAddr}/")
        self.db = dbClient.overseer
    
    def getServers(self):
        serversIter = self.db.servers.find({},{'sid':1})
        servers = {'servers':[]}
        for server in serversIter:
            servers['servers'].append(server['sid'])
        return servers

    def getMaster(self):
        return self.db.servers.find_one({'master':True})

    def getSlaves(self):
        serversIter = self.db.servers.find({"slave":True})
        slaves = []
        for server in serversIter:
            slaves.append(server)
        return slaves

    def addServer(self, serverData):
        self.db.servers.insert_one(serverData)

    def editServer(self, serverData, serverID):
        self.db.servers.replace_one({'sid':serverID},serverData)

    def removeServer(self, serverID):
        self.db.servers.delete_one({'sid':serverID})

    def serverFromID(self, serverID):
        server = self.db.servers.find_one({'sid':serverID})
        return server
