import unittest, os, hashlib
import requests
from requests.auth import HTTPBasicAuth

class MyTestCase(unittest.TestCase):
    req_string = 'http://localhost:1500/file'
    os.system('make run')

    def testPutWithoutAuthorization(self):
        response = requests.put(self.req_string, data = "data")
        self.assertEqual(response.status_code, 401)

    def testGet(self):
        response = requests.get(self.req_string, auth=HTTPBasicAuth('test', 'test'))
        self.assertEqual(response.status_code, 404)

    def testDelete(self):
        response = requests.delete(self.req_string, auth=HTTPBasicAuth('test', 'test'))
        self.assertEqual(response.status_code, 204)

    def testPut(self):
        response = requests.put(self.req_string, auth=HTTPBasicAuth('test', 'test'), data='{"username":"xyz","password":"xyz"}')
        self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()
