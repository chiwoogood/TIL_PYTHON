t = int(input())
for i in range(t):
    a, b = map(int,input().split())
    print('#{0} {1} {2} '.format(i+1,a//b,a%b))