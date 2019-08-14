def splitter(string, l, m, n):
    return string[l:l]
def merge_the_tools(string, k):
    # for i in range(k):

    # for j in range(len(string)-1):
    #     if(string[j]!=string[j+1]):
    #         a.append(string[j]+string[j+1])
    #     else:
            
            
    # print(a)
    l=len(string)//k
    for i in range(l):
        t=''
        for c in string[i*k:i*k+k]:
            if c not in t: 
                t+=c
        print(t)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
