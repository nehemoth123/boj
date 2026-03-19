n1=int(input())
n2=list(map(int,input().split( )))
n3=list(map(int,input().split( )))
n2.sort()
s=0
for j in range(n1):
    s+=min(n2)*max(n3)
    n2.pop(n2.index(min(n2)))
    n3.pop(n3.index(max(n3)))
print(s)