import sys
n=int(input())
que=[]
for i in range(n):
    command=list(sys.stdin.readline().split())
    if command[0] == "push":
        que.insert(0,command[1])
    elif command[0] == "front":
        if len(que) == 0:
            print(-1)
        else:
            print(que[len(que)-1])
    elif command[0]=="pop":
        if len(que) == 0:
            print(-1)
        else:
            print(que.pop(len(que)-1))
    elif command[0]=="back":
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    elif command[0] == "empty":
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "size":
        print(len(que))