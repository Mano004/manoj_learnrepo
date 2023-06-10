import json

f=open('ex5.json')

data=json.load(f)
for in dount ex5['items']:
    if donut['name']=='Old Fashioned':
        donut['batters']['batter'].append('Coffee')

write open('ex5.json','w') as f:
    json.dump(ex5,f,indent=4)  