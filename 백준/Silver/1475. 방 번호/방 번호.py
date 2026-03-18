N = input()

n1= N.count("1")
n2= N.count("2")
n3= N.count("3")
n4= N.count("4")
n5= N.count("5")
n6= N.count("6")
n7= N.count("7")
n8= N.count("8")
n9= N.count("9")
n0= N.count("0")

n69=0
if (n6+n9)%2==0:
    n69=(n6+n9)//2
else:
    n69=(n6+n9)//2+1

reserve = n1
if reserve <= n2:
    reserve = n2
if reserve <= n3:
    reserve = n3
if reserve <= n4:
    reserve = n4
if reserve <= n5:
    reserve = n5
if reserve <= n69:
    reserve = n69
if reserve <= n7:
    reserve = n7
if reserve <= n8:
    reserve = n8
if reserve <= n0:
    reserve = n0
    
print(reserve)