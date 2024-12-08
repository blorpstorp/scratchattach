import scratchattach as sa
import os
import json

session = sa.login_by_id(".eJxVkEFvgzAMhf8L58FCQiDtrZOmatI0rXSH7RSZxEBKSRAEoW3af18i9dKLZb1nf8_yb7IuOFsYMdkn5-_F4yg_k4fEuwFtkDjTGiqCipW6yJE3LShAFTqqSKj744d1p3VKz5eXmh-hfu_SU_6ads_LFjBX1xmbmimQKBEZExmlPBMsWBJW38uYLo0OfkkKVpScBEtfwHZOejPij7PxssOIs1Hw-Iab_HLzcL_fw9KHoYZUbY4EBdtVLW1ahYQjz3cCgTPKdcUE5CWJ4R4Xr5wbTIRvAYj6HtmACg-Id0UNrQ_p3jib3Ywlq3G63sSn2_DfP5-8bEc:1tJgno:tk_HIoq_NbcZopJ-wEivgYTRX4w", username="System_X")
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
            if data["password"] == password and not data["rank"] == "Unverified":
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

client.start()
