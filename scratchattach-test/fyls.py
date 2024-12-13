import os
import json
import scratchattach as scratch3

session = scratch3.login_by_id(".eJxVkEFvgzAMhf8L58FCQiDtrZOmatI0rXSH7RSZxEBKSRAEoW3af18i9dKLZb1nf8_yb7IuOFsYMdkn5-_F4yg_k4fEuwFtkDjTGiqCipW6yJE3LShAFTqqSKj744d1p3VKz5eXmh-hfu_SU_6ads_LFjBX1xmbmimQKBEZExmlPBMsWBJW38uYLo0OfkkKVpScBEtfwHZOejPij7PxssOIs1Hw-Iab_HLzcL_fw9KHoYZUbY4EBdtVLW1ahYQjz3cCgTPKdcUE5CWJ4R4Xr5wbTIRvAYj6HtmACg-Id0UNrQ_p3jib3Ywlq3G63sSn2_DfP5-8bEc:1tJgno:tk_HIoq_NbcZopJ-wEivgYTRX4w", username="System_X")
cloud = session.connect_cloud("943334414")
client = cloud.requests()


@client.request
def ping():
  print("recieved server check")
  return "pong"


@client.request
def adduser(argument1):
  if os.path.exists(f'{argument1}.json'):
    print("loading data")
    with open(f"{argument1}.json", "r") as f:
      data = json.load(f)
    return [data["rarities"], data["rolls"]]
    
  else:
    print("added user")
    with open(f'{argument1}.json', 'w') as f:
      json.dump({
          "username": argument1,
          "rolls": "0",
          "rarities": ""
      },
                f,
                indent=4)
      return "user added"


@client.request
def setdata(argument1, argument2, argument3):
  print("setting data")
  with open(f"{argument1}.json", "r") as f:
    data = json.load(f)

  data["rarities"] = argument2
  data["rolls"] = argument3

  with open(f'{argument1}.json', "w") as f:
    json.dump(data, f, indent=4)
    return "data set"


@client.request
def test1(argument1):
  print(argument1)
  return "finished test"


@client.event
def on_ready():
  print("Request handler is running")


client.start()
