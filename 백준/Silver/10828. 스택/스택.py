import sys
n=int(input())
stack = []
stack_number = 0
for i in range(n):
    command = list(sys.stdin.readline().split())
    if command[0] == "push":
        stack.append(command[1])
        stack_number += 1
    elif command[0] == "pop":
        if stack_number == 0:
            print(-1)
        else:
            print(stack.pop(stack_number-1))
            stack_number -=1
    elif command[0] == "top":
        if stack_number == 0:
            print(-1)
        else:
            print(stack[stack_number-1])
    elif command[0] == "empty":
        if stack_number == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "size":
        print(stack_number)