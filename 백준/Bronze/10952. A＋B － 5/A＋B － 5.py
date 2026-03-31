import sys
while True:
    a=list(map(int,sys.stdin.readline().split()))
    if a[0]+a[1]==0:
        break
    print(a[0]+a[1])