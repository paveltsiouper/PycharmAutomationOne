import requests
import json
from DataDrivenFramework import Library

def test_post_datadriven_request():
    """DataDriven request to create new student info using Excell spreadsheet"""
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    file = open("C:/Users/pault/PycharmProjects/PycharmAPIAutomationOne/DATA/CreateStudentInfoOne.json", 'r');
    json_request = json.loads(file.read())

    obj = Library.Common("C:/Users/pault/PycharmProjects/PycharmAPIAutomationOne/DATA/DataDriven.xlsx","StudentInfo")
    col=obj.fetch_column_count()
    rows=obj.fetch_row_count()
    keyList=obj.fetch_key_names()

    for i in range(2,rows+1):
        updated_json_request=obj.update_request_with_data(i,json_request,keyList)
        responce=requests.post(API_URL,updated_json_request)
        print(responce.text)
        print(responce.status_code)
        assert responce.status_code == 201

        # cell_first_name=sh.cell(row=i,column=1).value
        # cell_mid_name = sh.cell(row=i, column=2).value
        # cell_last_name = sh.cell(row=i, column=3).value
        # cell_dob = sh.cell(row=i, column=4).value
        # json_request['first_name'] = cell_first_name
        # json_request['middle_name'] = cell_mid_name
        # json_request['last_name'] = cell_last_name
        # json_request['date_of_birth'] = cell_dob
        # responce = requests.post(API_URL, json_request)
