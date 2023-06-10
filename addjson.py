import json
file = open ( 'ex5.json')
data = json.load(file)
ex5 = dict(enumerate(data))
for key,value in ex5.items():
    if key == " name " and value == " Old Fashioned":
         result = [{ " batter " :  [{ " id " : " 1003" , "type" : " coffee"}]}]
         ex5["batters" ] .update( result)
print(ex5)
