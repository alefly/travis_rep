import repository

def get(file):
	inCache = repository.checkCache(file)
	if inCache:
		return repository.getFromCache(file)
	inDB = repository.checkDB(file)
	if inDB:
		data = repository.getFromDB(file)
		repository.addToCache(file, data)
		return data
	return -1

def delete(file):
	if(repository.checkCache(file)):
		repository.deleteFromCache(file)
	repository.deleteFromDB(file)

def put(file, data):
	delete(file)
	repository.addToDB(file, data)
