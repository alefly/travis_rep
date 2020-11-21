from flask import Flask, request
import json
import service
import hashlib

app = Flask(__name__)

@app.route('/<file>', methods=['GET', 'PUT', 'DELETE'])
def storage(file):
	auth = request.authorization
	if not auth or not auth.username or not auth.password or service.authorization(auth.username, hashlib.md5(auth.password.encode()).digest()) == False:
		return 'Authorization is failed', 401
	if request.method == 'GET':
		resp = service.get(file)
		if(resp == -1):
			return 'File not found', 404
		else:
			return resp['value'], 200
	if request.method == 'DELETE':
		service.delete(file)
		return 'File deleted', 204
	if request.method == 'PUT':
		try:
			json.loads(request.data)
		except:
			return 'JSON isn`t right!', 400
		service.put(file, request.data)
		return 'File changed', 201
	return 'Error on server', 405

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080)
