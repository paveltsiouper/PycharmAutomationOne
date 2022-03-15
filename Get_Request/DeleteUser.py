import requests
#API URL
url="https://reqres.in/api/users/2"
response_delete_user2 = requests.delete(url)
print(response_delete_user2)
print(response_delete_user2.status_code)
assert response_delete_user2.status_code==204
print(response_delete_user2.headers)
print(response_delete_user2.content)