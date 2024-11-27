import scratchattach as sa
import os
import json

session = sa.login_by_id("SESSID", username="System_X")
cloud = session.connect_cloud("1100926253")
client = cloud.requests()

@client.request
def ping():
    print("Ping request received")
    return "pong"

@client.request
def sent(message, username):
    with open("messages.json", "r") as f:
        data = json.load(f)

    data[username] = message

    with open('messages.json', "w") as f:
        json.dump(data, f, indent=4)
        return "message sent"

@client.request
def get_messages():
    print("message request sent")
    with open('messages.json', "r") as f:
        data = json.load(f)
        print(data)
        return data

@client.request
def createuser(username, password):
    if not(os.path.exists(f'{username}.json')):
        with open(f"{username}.json", "w") as f:
            json.dump({
                  "password": password,
                  "rank": "Unverified"
              },
                        f,
                        indent=4)
            return "added"
    else:
        return "already exists"

@client.request
def log_in(username, password):
    if not(os.path.exists(f'{username}.json')):
        return "no user found"
    else:
        with open(f"{username}.json", "r") as f:
            data = json.load(f)
            if data["password"] == password:
                 return "logged in"
            else:
                return "wrong password/unverified account"

@client.request
def isadmin(username):
    with open(f"{username}.json", "r") as f:
        data = json.load(f)
        if data["rank"] == "Admin":
            return "is admin"

@client.request
def deleteaccount(username):
    if os.path.exists(f'{username}.json'):
        os.remove(f'{username}.json')
        return "deleted"
    else:
        return "no user found"

@client.request
def clearchat():
    with open('messages.json', "w") as f:
        json.dump({}, f, indent=4)
        return "cleared"

@client.event
def on_ready():
    print("Request handler is running")

client.run()
