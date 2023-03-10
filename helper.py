from flask import json

# this function will load all the 
# members from my members.json file
def load_members():
  with open("members.json") as file:
    MEMBERS = json.load(file)

  return MEMBERS