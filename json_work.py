import os
import json
ls=[]
for file in os.listdir("daaset"):
    content=open(os.path.join("daaset",file),"r")
    lines = content.read()
    ls.append(lines)

dict={'text':'hello'}
for i in ls:
    dict.update(text=i)
    with open('data.json', 'a') as outfile:  
        outfile.write(json.dumps(dict))
        outfile.write("\n")
