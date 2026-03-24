a=list(map(int,input().split( )))
b=list(map(int,input().split( )))
c=[]
for i in range(a[0]):
   if b[i]<a[1]:
       c.append(b[i])
for j in c:
    print(j,end=" ")