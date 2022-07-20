t = int(input())
for i in range(t):
    a, b = map(int,input().split())
    print('#{0}'.format(i+1),end=' ')
    if a > b:
        print('>')
    elif a < b:
        print('<')
    else:
        print('=')