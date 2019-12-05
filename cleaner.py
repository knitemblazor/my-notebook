
import pandas as pd

def cleaner(srt_file,lang):
    f = open(srt_file, 'r')
    x= f.read().splitlines()
    f.close()
#print(x)
    d =[]
    elim=['1','2','3','4','5','6','7','8','9','0',':',';','>','<','/',',','-','\\','#']
    for i in x:
        sent = " ".join("".join(["" if ch in elim else ch for ch in i]).split())
        d.append(sent)
#print(d)
    sentence=[]
    for i in d:
        if (len(i)!=0):
            sentence.append(i)
    #print(sentence)
    final=[]
    final.append(lang)
    final.append(sentence)
    return(final)

stoplist = set('for a of the and to in'.split()) # will strightaway remove these words

ls1=cleaner("eng.srt","english")
ls2=cleaner("french.srt","french")
collection=[]
collection.append(ls1)
collection.append(ls2)
todf=dict(collection)
df=pd.DataFrame(todf)
df.to_csv(r'data.csv')

