import json

with open("trackwins1.json") as f:
  data = json.load(f)


wins1 = data["player1"]
wins2 = data["player2"]
wins2 += 1

track = {}
track["player1"] = wins1
track["player2"] = wins2

f = open("trackwins1.json","w")
json.dump(track,f)
close(f)
print(wins1)
print(wins2)