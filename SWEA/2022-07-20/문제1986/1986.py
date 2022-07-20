import sys

sys.stdin = open("input.txt", "r")

n = int(input())

for i in range(n):
    num = 0
    s = int(input())
    for j in range(1,s+1):
        if j % 2 == 1:
            num += j
        else :
            num -= j
    print('#{0} {1}'.format(i+1,num))