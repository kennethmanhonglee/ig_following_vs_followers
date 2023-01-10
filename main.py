import json
from pprint import pprint

with open('following.json') as following, open('followers.json') as followers:
  following = json.load(following)["relationships_following"]
  followers = json.load(followers)["relationships_followers"]

  followers_cache = set()

  not_following_me = []

  for item in followers:
    followers_cache.add(item["string_list_data"][0]["value"])
  
  for person in following:
    ig_handle = person["string_list_data"][0]["value"]
    if ig_handle not in followers_cache:
      not_following_me.append(ig_handle)
  
  pprint(not_following_me)