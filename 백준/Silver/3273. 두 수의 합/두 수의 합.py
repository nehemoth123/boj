N1=int(input())
N2=list(map(int,input().split()))
N3=int(input())
N2.sort()
left=0
right=N1-1
ac=0
while left<right:
    ca=N2[left]+N2[right]
    if ca==N3:
        ac+=1
        left+=1
    elif ca>=N3:
        right-=1
    else:
        left+=1
print(ac)