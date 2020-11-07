from flask import Flask, request
import requests, sys
                                                                                                                                                                                

app = Flask(__name__)                                                           


@app.route('/<file>', methods=['GET', 'PUT', 'DELETE'])                         
def storage(file):
        try:
                port = '8080'
                name = 'server1'
                if len(file) % 2 == 0:
                        port = '8081'
                        name = 'server2'
                if request.method == 'GET':
                        response = requests.get('http://' + name + ':' + port + '/storage/' + file)
                if request.method == 'DELETE':
                        response = requests.delete('http://' + name + ':' + port + '/storage/' + file)
                if request.method == 'PUT':
                        response = requests.put('http://' + name + ':' + port + '/storage/' + file, data = request.data)
                if response.status_code >= 400:
                        return response.text, response.status_code
                if response.status_code != 200:
                        return 'OK!', response.status_code
                return response.text, 200
        except:
                return sys.exc_info()[0], 505

if __name__ == '__main__':                                                      
        app.run(host='0.0.0.0', port=8082)
