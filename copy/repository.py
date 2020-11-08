import redis, pymongo


cache = redis.Redis(host='redis', port=6379, decode_responses=True, health_check_interval=30)
mongoClient = pymongo.MongoClient(host='mongo', port=27017)
mongo_table = mongoClient['hw9_1']['files']
cache.ping()

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
