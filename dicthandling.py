#https://www.hackerrank.com/challenges/nested-list/problem?h_r=next-challenge&h_v=zen
# find the name of students with 2nd least score
# Sample Input 0

# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39

# Sample Output 0

# Berry
# Harry




if __name__ == '__main__':
    record=[]
    for _ in range(int(input())):
        entry=[]
        name = input()
        score = float(input())
        entry.append(name)
        entry.append(score)
        record.append(entry)
    marks=list(dict(record).values()) #converting kist of list to dicts
    marksd=dict(record)
    marks.sort()
    # print(marks)
    a=set(marks)  #set removes multiple copies from list set can be further converted to list
    # print(a)
    marks=list(a)
    marks.sort()
    nam=[]
    for name, mark in marksd.items():    
        if mark==marks[1]:
            nam.append(name)

    nam.sort()
    for i in nam:
        print(i)

