import requests
import json
import jsonpath

def test_end_to_end():
    API_URL="http://thetestingworldapi.com/api/studentsDetails"
    file=open("C:/Users/pault/PycharmProjects/PycharmAPIAutomationOne/DATA/CreateStudentInfoOne.json",'r');
    json_request=json.loads(file.read())
    response=requests.post(API_URL,json_request)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(response.text)
    print(id[0])

    API_URL = "http://thetestingworldapi.com/api/technicalskills"
    file = open("C:/Users/pault/PycharmProjects/PycharmAPIAutomationOne/DATA/postEndToEndTechSkills.json", 'r');
    json_request = json.loads(file.read())
    json_request['id']=int(id[0])
    json_request['st_id'] = str(id[0])
    response = requests.post(API_URL, json_request)
    print(response.text)


    API_URL_Tech="http://thetestingworldapi.com/api/addresses"
    file = open("C:/Users/pault/PycharmProjects/PycharmAPIAutomationOne/DATA/postEndToEndTechAdresses.json", 'r');
    json_request = json.loads(file.read())
    json_request["stId"]=str(id[0])
    response = requests.post(API_URL_Tech, json_request)
    print(response.text)

    API_URL_Final_Details="http://thetestingworldapi.com/api/FinalStudentDetails/"+str(id[0])
    response = requests.get(API_URL_Final_Details)
    print(response.text)