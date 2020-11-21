import repository

def authorization(login,password):
	if repository.userInDB(login)['value'] == password:
		return True
	return False

def get(file):
	data = repository.getFromCache(file)
	if data:
		return data
	data = repository.getFromDB(file)
	if data:
		return data
	return -1

def delete(file):
	if(repository.checkCache(file)):
		repository.deleteFromCache(file)
	repository.deleteFromDB(file)

def put(file, data):
	delete(file)
	repository.addToDB(file, data)
