import json,ast 
import time

with open("data2.json")as file:
    js=json.loads(file.read())

t1 = time.time()
for page in js:
    for label in js[page]:
        for info in js[page][label]:
            for ent in js[page][label][info]:
                if(label=="billing address" or label=="shipping_address" or label=="vendors_address"):
                    #print(ent)
                    if(ent == "AMOUNT" or ent == "DATE" or ent == "PURCHASE_ORDER"):
                        js[page][label][info]
                        if "AMOUNT" in js[page][label][info]:
                            del js[page][label][info]["AMOUNT"]
                        if "DATE" in js[page][label][info]:
                            del js[page][label][info]["DATE"]
                        if "PURCHASE_ORDER" in js[page][label][info]:
                            del js[page][label][info]["PURCHASE_ORDER"]
                        break
                   
                     

t2 = time.time()
#if "AMOUNT" in js2:
#del js2["AMOUNT"]
print(t2-t1)
jdata = ast.literal_eval(json.dumps(js))
print(jdata)
#print(type(js2))
with open("final2.json","w") as file:
    file.write(json.dumps(jdata))
