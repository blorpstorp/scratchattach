import scratchattach as scratch3
import json
import os

session = scratch3.login_by_id("SESS_ID", username="System_X")
cloud = session.connect_cloud("943334414")
client = cloud.requests()

@client.request
def ping():
  print("recieved server check")
  return "pong"


@client.request
def signupdep(argument1):
  with open("signup.txt", "r+") as f:
    data = f.read()
    if argument1 in data:
      print("user already exists")
      return "already exists"
    else:
      f.write("\n" + argument1)
  print("recieved signup request")
  return "signup complete"


@client.request
def clientping():
  print("recieved client check")
  return "clientpong"


@client.request
def checkuserdep(argument1):
  with open("accounts.txt", "r") as f:
    data = f.read()
    if argument1 in data:
      return "user exists"
    else:
      return "user does not exist"


@client.request
def checkuser(argument1):
  with open(f"{argument1}.json", "r") as f:
    data = json.load(f)
    return data['username'], data['accounttype']

@client.request
def notifs(argument1):
  with open(f"{argument1}.json", "r") as f:
    data = json.load(f)
    return data['notifications']


@client.request
def signup(argument1):
  with open(f'{argument1}.json', 'w') as f:
    json.dump(
        {
            "username": argument1,
            "accounttype": "unverified",
            "notifications": "",
            "requests": "",
            "isAdmin": "false"
        },
        f, 
        indent=4)
    return "user added"

@client.request
def setdata(argument1, argument2):
  with open(f"{argument1}.json", "r") as f:
    data = json.load(f)

  data["requests"] = argument2

  with open(f'{argument1}.json', "w") as f:
            json.dump(data, f, indent=4)
            return "data set"


@client.event
def on_ready():
  print("Request handler is running")


client.start()
