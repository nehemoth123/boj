l=list(map(int,input().split()))
s=[0,0,0,0,0,0,0,0,0,0,0,0]

for i in range(l[0]):
    i=list(map(int,input().split()))
    if i==[0,1]:
        s[0]+=1
    elif i==[1,1]:
        s[1]+=1
    elif i==[0,2]:
        s[2]+=1
    elif i==[1,2]:
        s[3]+=1
    elif i==[0,3]:
        s[4]+=1
    elif i==[1,3]:
        s[5]+=1
    elif i==[0,4]:
        s[6]+=1
    elif i==[1,4]:
        s[7]+=1
    elif i==[0,5]:
        s[8]+=1
    elif i==[1,5]:
        s[9]+=1
    elif i==[0,6]:
        s[10]+=1
    else:
        s[11]+=1
r=0
for j in range(12):
    if s[j-1]%l[1]!=0:
        r+=s[j-1]//l[1]+1
    else:
        r+=s[j-1]//l[1]
print(r)