import requests
import sys
    
user_name = input("Enter the Github username you want to know about: ")

if not user_name:
    print("Please provide ab username")
    sys.exit()

response = requests.get(f"https://api.github.com/users/{user_name}/events")

# creating list of dictionary from the received requests
response_dicts = response.json()

seet = set()

id = 0
for respone in response_dicts:
    id += 1
    # repo name:
    print("*"*50)
    print(f"S.NO- {id}")
    repo = respone['repo']
    payload = respone['payload']
    print(f"Repo: {repo['name']}-{repo['id']}")
    # print(f"Action: {payload['action']}")
    print(f"Created on {respone['created_at']}")
    action = respone['type']
    if action == 'Watch0Event':
        print(f"Repo Starred")
    else:
        print(f'Type: {action}')
        seet.add(action)

    # org details
    try:
        if respone['org']:
            print(f"Org: {respone['org']['login']}")
    except:
        print()
    finally:
        print("*"*50)
    print('')

print(f"Total Repo that {user_name} worked on: {id}")
print(seet)