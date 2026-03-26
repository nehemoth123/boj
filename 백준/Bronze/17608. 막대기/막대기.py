import sys
n =int(sys.stdin.readline())
list=[]
for i in range(n):
    reserve =int(sys.stdin.readline())
    list.append(reserve)
reserve_2 = list[-1]
nc=1
for j in range(n):
    if reserve_2<list[-j-1]:
        nc+=1
        reserve_2=list[-j-1]
    
print(nc)