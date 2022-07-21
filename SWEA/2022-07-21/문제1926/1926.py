# import sys

# sys.stdin = open("input.txt", "r")
n = int(input())
k = len(str(n))
for i in range(1,n+1):
    i = str(i)
    for j in range(len(i)):
        if i[j] == '1' or i[j] == '2' or i[j] == '4' or i[j] == '5' or i[j] == '7' or i[j] == '8' or i[j] == '0' :
            print('{0}'.format(i),end = ' ')
        elif i[j] == '3' or i[j] == '6' or i[j] == '7' :
            print('-', end = ' ')
        else:
            print('-', end = ' ')



        
#시간내에 못풀었다

    




    