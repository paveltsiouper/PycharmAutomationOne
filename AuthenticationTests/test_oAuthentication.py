import requests
import json
import jsonpath

def test_oath_api():
    Token_Url="http://thetestingworldapi.com/Token"
    token_data={'grant_type':'password','username':'admin','password':'adminpass'}
    response=requests.post(Token_Url,token_data)
    print(response.text)
    response_access_token=jsonpath.jsonpath(response.json(),'access_token')
    print(response_access_token[0])
    authorization_token={'Authorization':'Bearer '+response_access_token[0]}
    print(authorization_token)
    API_URL='http://thetestingworldapi.com/api/StDetails/1104'
    response=requests.get(API_URL,headers=authorization_token)
    print(response.text)