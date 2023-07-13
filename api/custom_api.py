import requests, pprint, json, inquirer
pp = pprint.PrettyPrinter(indent=5)

url = "https://f4idu2pd8h.execute-api.us-east-1.amazonaws.com/v1/info"
headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,X-Amz-Security-Token",
        "Access-Control-Allow-Origin*": "*"
}

resp = requests.get(url, headers=headers)
data = resp.json()['body']

info = json.loads(data)
sessions = info[1]
#pp.pprint(info)

# for staff in info[0]['staff']:
#     if staff['name'] == 'Abdul Sharif':
#         print(f"Abdul is currently {staff['title']}")

print(sessions)
