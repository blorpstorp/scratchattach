import scratchattach as scratch3
import os
import json

session = scratch3.login_by_id("", username="System_X")
cloud = session.connect_cloud("979495530")
client = cloud.requests()

@client.request
def ping():
  print("recieved server check")
  return "pong"

@client.request
def getsellreq():
  with open("data.json", "r") as f:
    data = json.load(f)
    print("got data")
    return data["id1"]

@client.event
def on_ready():
  print("Request handler is running")


client.start()
