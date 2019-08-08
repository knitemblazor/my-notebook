#https://www.hackerrank.com/challenges/nested-list/problem?h_r=next-challenge&h_v=zen
if __name__ == '__main__':
    record=[]
    for _ in range(int(input())):
        entry=[]
        name = input()
        score = float(input())
        entry.append(name)
        entry.append(score)
        record.append(entry)
    marks=list(dict(record).values())
    marksd=dict(record)
    marks.sort()
    # print(marks)
    a=set(marks)
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

