n = int(input())
for i in range(n):
    a, b = map(int,input().split())
    print('#{0} {1} {2}'.format(i+1, int(a / b), a % b))