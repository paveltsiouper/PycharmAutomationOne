
import requests
#API URL
url="https://httpbin.org/get"
params={"ParamOne":"ParamOneValue","ParamTwo":"ParamTwoValue"}
response_get_customheaders = requests.get(url,params=params)
print(response_get_customheaders)
print("text********")
print(response_get_customheaders.text)