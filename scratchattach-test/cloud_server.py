import scratchattach as scratch3
import json
import os

session = scratch3.login_by_id(".eJxVkEFvgzAMhf8L58FCQiDtrZOmatI0rXSH7RSZxEBKSRAEoW3af18i9dKLZb1nf8_yb7IuOFsYMdkn5-_F4yg_k4fEuwFtkDjTGiqCipW6yJE3LShAFTqqSKj744d1p3VKz5eXmh-hfu_SU_6ads_LFjBX1xmbmimQKBEZExmlPBMsWBJW38uYLo0OfkkKVpScBEtfwHZOejPij7PxssOIs1Hw-Iab_HLzcL_fw9KHoYZUbY4EBdtVLW1ahYQjz3cCgTPKdcUE5CWJ4R4Xr5wbTIRvAYj6HtmACg-Id0UNrQ_p3jib3Ywlq3G63sSn2_DfP5-8bEc:1tJgno:tk_HIoq_NbcZopJ-wEivgYTRX4w", username="System_X")
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

@client.request
def sendnotif(username, notif):
  with open(f"{username}.json", "r") as f:
    data = json.load(f)

  data["notifications"] = notif

  with open(f'{username}.json', "w") as f:
    json.dump(data, f, indent=4)
    return "sent notif"

@client.request
def isuseradmin(username):
  with open(f"{username}.json", "r") as f:
    data = json.load(f)

  if data["isAdmin"] == "true":
    return "is admin"
  else:
    return "is not admin"

@client.request
def verifyuser(username):
  with open(f"{username}.json", "r") as f:
    data = json.load(f)

  data["accounttype"] = "verified"

  with open(f'{username}.json', "w") as f:
    json.dump(data, f, indent=4)
    return "verified"

@client.event
def on_ready():
  print("Request handler is running")


client.start()
