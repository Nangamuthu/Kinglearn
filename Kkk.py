import json

with open('2nd assignment\Ext.json','r') as file:
    Ext = json.load(file)
    #print("Printing the JSON File:\n",Ext)
    
for i in Ext:
    
    if i['name'] == 'Old Fashioned':
        x=i['batters']['batter']
        
        max_id=0
        for id in x:
            cur_id = int(id["id"])
            if cur_id > max_id:
                max_id = cur_id
        last_id=str(max_id + 1)
        z={ "id": last_id, "type": "Coffee" }
        x.append(z)
        
print("\nAfter adding 'Coffee' to JSON File:\n",Ext)

with open('2nd assignment\Ext.json','w') as out:
    json.dump(Ext,out,indent=4)
