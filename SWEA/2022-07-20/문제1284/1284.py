import sys

sys.stdin = open("input.txt", "r")

N = int(input())
for i in range(N):
    A = 0
    B = 0
    P, Q, R, S, W = map(int,input().split())
    for s in range(W):
        A += P
    if W <= R:
        for j in range(R):
            B += Q
    else:
        for l in range(R):
            B += Q
        for k in range(W-R):
            B += S
    print('#{0} {1}'.format(i+1,min(A,B)))
