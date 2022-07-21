import sys

sys.stdin = open("input.txt", "r")
n = int(input())

for i in range(n):
    t1 ,m1 ,t2 ,m2 = map(int,input().split())
    t3 = t1 + t2
    m3 = m1 + m2
    if m3 >=60 :
        m3 -= 60
        t3 += 1
    if t3 > 12:
        t3 -= 12

    print('#{0} {1} {2}'.format(i+1, t3 ,m3))