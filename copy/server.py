from flask import Flask
from flask import abort, request
import io
import os.path
import json

app = Flask(__name__)

@app.route('/storage/<file>', methods=['GET', 'PUT', 'DELETE'])
def storage(file):
	if request.method == 'GET':
		if os.path.exists(file):
			return io.open(file).read()
		else:
			abort(404)
		if request.method == 'DELETE':
			if os.path.exists(file):
				os.remove(file)
			return '', 204
		if request.method == 'PUT':
			try:
				data = json.loads(request.data)
			except:
				abort(400)
	f = io.open(file, 'w')
	f.write(request.data.decode('utf-8'))
	return '', 201
	
	
if __name__ == '__main__':
	app.run(port = 8080)

