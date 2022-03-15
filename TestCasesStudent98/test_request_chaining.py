import requests
import json
import jsonpath

def test_request_chaining():
    global id
    API_URL="http://thetestingworldapi.com/api/studentsDetails"
    file=open("C:/Users/pault/PycharmProjects/PycharmAPIAutomationOne/DATA/CreateStudentInfoOne.json",'r');
    json_request=json.loads(file.read())
    response=requests.post(API_URL,json_request)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(response.text)
    print(id[0])

def test_get_student():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/"+str(id[0])
    response = requests.get(API_URL)
    print(response.text)