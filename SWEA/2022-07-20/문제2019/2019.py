import sys

sys.stdin = open("input.txt", "r")

n = int(input())
num = 1
print(num,end = ' ')
while n > 0:
    num = num * 2
    n -= 1
    print(num,end=' ')


    