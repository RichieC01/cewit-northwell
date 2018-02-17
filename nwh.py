import requests, json

url = 'https://apim-hie-dev.azure-api.net/restsda/patient/SDA'
data = {
    'AssigningAuthority':'NSMG',
    'MRN' : '541276'
 }
headers = {
    # Request headers
    'Requestor': 'request',
    # 'Content-Type': 'application/json',
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'ad108eefd75549898aac1908c3cd9265',
}
r = requests.post(url, data=json.dumps(data), headers=headers)
response = r.text
print(response)
