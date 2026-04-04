import json

with open('obj.json','r') as f:

   d= json.load(f)
   print(d)
   print(type(d))