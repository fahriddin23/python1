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

session_choices = [
    inquirer.List('name', message="Choose a session", choices=[x['name'] for x in sessions['sessions']])
]

user_selection = inquirer.prompt(session_choices)

for x in sessions['sessions']:
    if x['name'] == user_selection['name']:

        print(f"""
********* Info for {user_selection['name']} *********

- Duration: {x['duration']}
- Prerequisets: {x['prerequisets']}
- Certificates: {x['certificates']}
- Instructor: {x['instructor']}
- Price: {x['price']}
          
""")
