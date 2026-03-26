
T=int(input())
for i in range(T):
    pscount=[]
    isitvps=input()
    for j in isitvps:
        if j == "(":
            pscount.append(j)
        else:
            if pscount:
                pscount.pop()
            else:
                print("NO")
                break
    else:                
        if not pscount:
            print("YES")
        else:
            print("NO")
    
    