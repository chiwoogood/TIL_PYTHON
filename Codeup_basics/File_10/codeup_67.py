s = int(input())
if s > 0:
    if s % 2 == 0:
        print('C')
    else:
        print('D')
else:
    if s < 0:
        if s % 2 == 0:
            print('A')
        else:
            print('B')