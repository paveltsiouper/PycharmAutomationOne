import json

import jsonpath
import requests
#API URL
url="https://reqres.in/api/users?page=2"
response_get_users = requests.get(url)
print(response_get_users)
print(response_get_users.status_code)
assert response_get_users.status_code==200
print(response_get_users.headers)
print(response_get_users.content)

#fetch response header
print(response_get_users.headers)
print(response_get_users.headers.get('Date'))
print(response_get_users.headers.get('Server'))
#fetch cookies
#url="https://reqres.in/api/users";
response_get_users = requests.get(url)
print(response_get_users.cookies)
print(response_get_users.encoding)
print(response_get_users.elapsed)

#parse rsponce JSON format
json_response_get_users=json.loads(response_get_users.text)
print(json_response_get_users)
print(json_response_get_users.get('page'))
print(json_response_get_users.get('data')[0].get('id'))
user_one=json_response_get_users.get('data')[0]
print(user_one.get('email'))

first_name=jsonpath.jsonpath(user_one,'first_name')
print(first_name[0])
data_first_name=jsonpath.jsonpath(json_response_get_users,'data[0].first_name')
print(data_first_name)
data_first_name2=jsonpath.jsonpath(json_response_get_users,'data[2].first_name')
print(data_first_name2)
print("******************************")
print(jsonpath.jsonpath(json_response_get_users,'data')[0])
print(len(jsonpath.jsonpath(json_response_get_users,'data')[0]))
print("******************************")
for i in range(0,len(jsonpath.jsonpath(json_response_get_users,'data')[0])):
    first_name=jsonpath.jsonpath(json_response_get_users,'data['+str(i)+'].first_name')
    print(first_name)