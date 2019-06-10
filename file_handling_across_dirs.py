import shutil
d=[]
for image in os.listdir("/media/her/bh/images_to_json/images"):
    if image not in e:
        d.append(image)

for image in d:
    f="/media/her/bh/images_to_json/images/"+str(image)
    g="/media/her/bh/images_to_json/images_undetected/"+str(image)
    shutil.copyfile(f ,g)  
