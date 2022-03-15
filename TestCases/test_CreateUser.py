import os
import requests
import json
import jsonpath
import pytest

url="https://reqres.in/api/users"
a=101

# @pytest.fixture
# def start_exec():
#     global file_data_post_user
#     file_data_post_user = open("./../DATA/user_one", 'r')
@pytest.fixture
def start_exec(scope='module'):
    global file_data_post_user
    file_data_post_user = open("./../DATA/user_one", 'r')

@pytest.mark.skip("This is not current test case")
def test_create_new_user():
    CURR_DIR=os.getcwd()
    print("***********????")
    print(CURR_DIR)
    print("***********????")
    file_data_post_user = open("./../DATA/user_one", 'r')
    userData = file_data_post_user.read()
    json_input = json.loads(userData)
    print(json_input)
    post_responce = requests.post(url, json_input)
    print(post_responce.content)  # b'{"name":"tester_one","job":"test_leader","id":"674","createdAt":"2022-02-24T19:26:15.510Z"}'
    json_responce = json.loads(post_responce.text)
    print(json_responce)  # {'name': 'tester_one', 'job': 'test_leader', 'id': '674', 'createdAt': '2022-02-24T19:26:15.510Z'}
    first_name = jsonpath.jsonpath(json_responce, 'name')
    print(first_name[0])
    print(jsonpath.jsonpath(json_responce, 'job')[0])
    print(jsonpath.jsonpath(json_responce, 'id')[0])
    assert post_responce.status_code == 202
    # Fetch header from report
    print(post_responce.headers)
    print("Server:" + post_responce.headers.get("Server"))

@pytest.mark.skipif(a>100, reason="Skipped testcase")
def test_create_second_user():
    CURR_DIR=os.getcwd()
    print("***********????")
    print(CURR_DIR)
    print("***********????")
    file_data_post_user = open("./../DATA/user_one", 'r')
    userData = file_data_post_user.read()
    json_input = json.loads(userData)
    print(json_input)
    post_responce = requests.post(url, json_input)
    print(post_responce.content)  # b'{"name":"tester_one","job":"test_leader","id":"674","createdAt":"2022-02-24T19:26:15.510Z"}'
    json_responce = json.loads(post_responce.text)
    print(json_responce)  # {'name': 'tester_one', 'job': 'test_leader', 'id': '674', 'createdAt': '2022-02-24T19:26:15.510Z'}
    first_name = jsonpath.jsonpath(json_responce, 'name')
    print(first_name[0])
    print(jsonpath.jsonpath(json_responce, 'job')[0])
    print(jsonpath.jsonpath(json_responce, 'id')[0])
    assert post_responce.status_code == 202
    # Fetch header from report
    print(post_responce.headers)
    print("Server:" + post_responce.headers.get("Server"))

@pytest.mark.Smoke
@pytest.mark.Regression
def test_create_third_user(start_exec):
    CURR_DIR=os.getcwd()
    print("***********????")
    print(CURR_DIR)
    print("***********????")
    #file_data_post_user = open("./../DATA/user_one", 'r')
    userData = file_data_post_user.read()
    json_input = json.loads(userData)
    print(json_input)
    post_responce = requests.post(url, json_input)
    print(post_responce.content)  # b'{"name":"tester_one","job":"test_leader","id":"674","createdAt":"2022-02-24T19:26:15.510Z"}'
    json_responce = json.loads(post_responce.text)
    print(json_responce)  # {'name': 'tester_one', 'job': 'test_leader', 'id': '674', 'createdAt': '2022-02-24T19:26:15.510Z'}
    first_name = jsonpath.jsonpath(json_responce, 'name')
    print(first_name[0])
    print(jsonpath.jsonpath(json_responce, 'job')[0])
    print(jsonpath.jsonpath(json_responce, 'id')[0])
    assert post_responce.status_code == 202
    # Fetch header from report
    print(post_responce.headers)
    print("Server:" + post_responce.headers.get("Server"))

@pytest.mark.Smoke
def test_create_fourth_user(start_exec):
    CURR_DIR=os.getcwd()
    print("create_fourth_user***********????")
    print(CURR_DIR)
    print("***********????")
    #file_data_post_user = open("./../DATA/user_one", 'r')
    userData = file_data_post_user.read()
    json_input = json.loads(userData)
    print(json_input)
    post_responce = requests.post(url, json_input)
    print(post_responce.content)  # b'{"name":"tester_one","job":"test_leader","id":"674","createdAt":"2022-02-24T19:26:15.510Z"}'
    json_responce = json.loads(post_responce.text)
    print(json_responce)  # {'name': 'tester_one', 'job': 'test_leader', 'id': '674', 'createdAt': '2022-02-24T19:26:15.510Z'}
    first_name = jsonpath.jsonpath(json_responce, 'name')
    print(first_name[0])
    print(jsonpath.jsonpath(json_responce, 'job')[0])
    print(jsonpath.jsonpath(json_responce, 'id')[0])
    assert post_responce.status_code == 201
    # Fetch header from reportclear

    print(post_responce.headers)
    print("Server:" + post_responce.headers.get("Server"))