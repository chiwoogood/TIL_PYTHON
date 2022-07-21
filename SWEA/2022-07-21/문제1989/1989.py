import sys

sys.stdin = open("input.txt", "r")
n = int(input())
for i in range(n):
    s = input()
    a = -1
    for j in s:
        if j == s[a]:
            a -= 1
        else:
            break
    if -a >= len(s)/2:
        print('#{0} {1}'.format(i+1,1))
    else:
        print('#{0} {1}'.format(i+1,0))





