import requests
import json
import jsonpath

def test_create_new_student():
    API_URL="http://thetestingworldapi.com/api/studentsDetails"
    file=open("C:/Users/pault/PycharmProjects/PycharmAPIAutomationOne/DATA/CreateStudentInfoOne.json",'r');
    json_request=json.loads(file.read())
    response=requests.post(API_URL,json_request)
    print(response.text)

def test_get_data():
    API_URL="http://thetestingworldapi.com/api/studentsDetails/1034701"
    response=requests.get(API_URL)
    print(response.text)
    json_response=json.loads(response.text)
    id=jsonpath.jsonpath(json_response,'data.id')
    print('id='+str(id[0]))
    assert id[0]==1032225, "Correct student id:"+str(id[0])

def test_put_request():
    API_URL="http://thetestingworldapi.com/api/studentsDetails/1034701"
    file = open("C:/Users/pault/PycharmProjects/PycharmAPIAutomationOne/DATA/PutStudentInfoOne.json", 'r');
    json_request = json.loads(file.read())
    response=requests.put(API_URL,json_request)
    print(response.text)
    #json_response=json.loads(response.text)
    response=requests.get(API_URL)
    print(response.text)

def test_get_data():
    API_URL="http://thetestingworldapi.com/api/studentsDetails/1034701"
    response=requests.delete(API_URL)
    print(response.text)
    json_response=json.loads(response.text)
