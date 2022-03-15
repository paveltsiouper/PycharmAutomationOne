import requests
import json
import jsonpath
url="https://reqres.in/api/users"
#userData ='{"name": "pablo_neruda","job": "painter"}';
file_data_post_user=open("./../DATA/user_one",'r')
userData=file_data_post_user.read()
json_input=json.loads(userData)
print(json_input)
post_responce = requests.post(url,json_input)
print(post_responce.content)  #b'{"name":"tester_one","job":"test_leader","id":"674","createdAt":"2022-02-24T19:26:15.510Z"}'
json_responce=json.loads(post_responce.text)
print(json_responce)#{'name': 'tester_one', 'job': 'test_leader', 'id': '674', 'createdAt': '2022-02-24T19:26:15.510Z'}
first_name=jsonpath.jsonpath(json_responce,'name')
print(first_name[0])
print(jsonpath.jsonpath(json_responce,'job')[0])
print(jsonpath.jsonpath(json_responce,'id')[0])

assert post_responce.status_code==201
#Fetch header from report
print(post_responce.headers)
print("Server:"+post_responce.headers.get("Server"))