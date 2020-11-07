from flask import Flask, request
import io, os.path, json, sys

app = Flask(__name__)

@app.route('/storage/<file>', methods=['GET', 'PUT', 'DELETE'])
def storage(file):
	if request.method == 'GET':
		if os.path.exists(file):
			return io.open(file).read()
		else:
			return 'File not found!', 404
	if request.method == 'DELETE':
		if os.path.exists(file):
			os.remove(file)
		return '', 204
	if request.method == 'PUT':
		try:
			data = json.loads(request.data)
		except:
			return 'JSON isn`t right!', 400
		f = io.open(file, 'w')
		f.write(request.data.decode('utf-8'))
		f.close()
		return '', 201
	return 'Error on server!', 405

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=int(sys.argv[1]))
