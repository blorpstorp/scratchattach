import os
import json
import scratchattach as scratch3

conn = scratch3.TwCloudConnection(project_id="972854590")
client = scratch3.TwCloudRequests(conn)


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
