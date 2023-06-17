import json


def write():
    with open('src\org.json','r') as file:
        ex5=json.load(file)

    for x in ex5:
        if x['type'] == "donut" and x['name'] == 'Old Fashioned':
            z=x['batters']['batter']
            z.append({'id': '1003', 'type': 'Coffee'})

    with open('src\org_out.json','w') as file:
        json.dump(ex5,file,indent=4)

def show_the_write():
    write()
    with open('src\org_out.json','r') as file:
        data=json.load(file)
    file.close()
    return data