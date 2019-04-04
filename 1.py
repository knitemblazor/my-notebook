
print("enter the sentence")
a=input()

#no. of  chars
a=a[:50]
length=len(str(a))
b=str(a).split()
print("no of chars:\n",length)
print("words:\n",b)
print("no of words:\n",len(b))

#occurances
occurances=[]
for i in b:
  count=0
  for j in b:
   	if(i==j):
          count=count+1
  occurances.append(count)
print("occurances",occurances)

#replace duplicate words with "***"
rep11=[]
for i in range (len(occurances)):
   if(occurances[i]>1):
     rep11.append("***")
   else:
     rep11.append(b[i])
rep1=" ".join(str(i) for i in rep11)
print("replaced repeated words with ***:\n",rep1)

#replace all occurances of e with zero
replacedstr=[]
for i in a:
  if(i=='e'):
    replacedstr.append(0)
  else:
    replacedstr.append(i)

rep2= "".join(str(i) for i in replacedstr)
print("replaced text with e to 0:\n",rep2)

#convert first letter of odd index pos words to upper and even indexed to lower case
rep3=[]
for i in range(len(b)):
   if(i%2==0):
     d=str(b[i])
     d=list(d)
     d[0]=str(d[0]).capitalize()
     f="".join(str(i) for i in d)
   else:
     f=str(b[i])
   rep3.append(f)

reps3=" ".join(str(i) for i in rep3)
print("convert first letter of odd index pos words to upper and even indexed to lower case:\n",reps3) 

#calculate no of uppercase
count1=0
count2=0
for i in reps3:
  if(i.isupper()):
     count1=count1+1
  else:
     count2=count2+1
print("uppercasecount",count1)
print("lowercasecount",count2)

#write to a file after sorting them alphabetically
reps4=reps3.split()
reps4.sort()
print(reps4.sort())
with open("first.txt",'w') as f:
   reps5="-".join(str(i) for i in b)
   f.write(reps5)
