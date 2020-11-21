import redis, pymongo
import hashlib

cache = redis.Redis(host='localhost', port=6379, decode_responses=True, health_check_interval=30)
mongoClient = pymongo.MongoClient(host='localhost', port=27017)
mongo_table = mongoClient['hw11_1']['files']
mongo_users = mongoClient['hw11_1']['users']
mongo_users.insert_one({'key':"alyona", 'value':(hashlib.md5('123'.encode())).digest()})
mongo_users.insert_one({'key':"admin", 'value':(hashlib.md5('admin'.encode())).digest()})
mongo_users.insert_one({'key':"user", 'value':(hashlib.md5('user'.encode())).digest()})
mongo_users.insert_one({'key':"test", 'value':(hashlib.md5('test'.encode())).digest()})
mongo_table.insert_one({"key": "file", "value":"test"})
cache.ping()

def userInDB(login):
    return mongo_users.find_one({'key': login})

def checkCache(file):
    return cache.exists(file)


def getFromCache(file):
    return cache.get(file)


def getFromDB(file):
    return mongo_table.find_one({'key': file})


def deleteFromCache(file):
    cache.delete(file)


def deleteFromDB(file):
    mongo_table.delete_many({'key': file})


def addToCache(file, data):
    cache.set(file, data)


def addToDB(file, data):
    mongo_table.insert_one({'key':file, 'value':data})
