import json
import jsonpath
import requests
#API URL
url="https://httpbin.org/get";
headers_custom={"CustomeHeaderOne":"customeheaderone value","CustomeHeaderTwo":"customeHeaderTwo = VALUE"}
response_get_customheaders = requests.get(url,headers=headers_custom);
print(response_get_customheaders);
print("text********")
print(response_get_customheaders.text);
print("code********")
print(response_get_customheaders.status_code);
assert response_get_customheaders.status_code==200
print("headers********")
print(response_get_customheaders.headers);
print("content********")
print(response_get_customheaders.content);


#parse rsponce JSON format
print("json_text********")
json_response_get_customheaders=json.loads(response_get_customheaders.text);
print(json_response_get_customheaders);
print("********")
customheaders_responce_customone=jsonpath.jsonpath(json_response_get_customheaders,'headers.Customeheaderone')
print(customheaders_responce_customone[0])
customheaders_responce_customtwo=jsonpath.jsonpath(json_response_get_customheaders,'headers.Customeheadertwo')
print(customheaders_responce_customtwo[0])