n=int(input())
l=list(map(int,input().split()))
t=int(input())
r=0
for i in range(len(l)):
    if l[i]==t:
        r+=1
print(r)