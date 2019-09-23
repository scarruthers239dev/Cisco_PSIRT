import requests
import json

url = "https://api.cisco.com/security/advisories/product"

querystring = {"product":"communications_manager"}

headers = {
    'Accept': "application/json",
    'Authorization': "Bearer XXXX",
    'User-Agent': "PostmanRuntime/7.17.1",
    'Cache-Control': "no-cache",
    'Postman-Token': "XXXX",
    'Host': "api.cisco.com",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.get(url, headers=headers, params=querystring)


jsonData = response.json()

strAdvisories = jsonData['advisories']

for i in strAdvisories:
    print("#########################################")
    print("Advisory_ID : " + i["advisoryId"])
    print("Severity : " + i["sir"])
    print("Advisory_Title : " + i["advisoryTitle"])
    print("Last_Updated_Date : " + i["lastUpdated"])


# jsonData = json.loads(response[0].text)

# print(jsonData)

# for i in jsonData:
#     print(i["advisory_id"])
