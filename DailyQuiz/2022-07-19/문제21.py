#주어진 숫자를 뒤집은 결과를 출력하시오. 
#* 문자열이 아닌 숫자로 활용해서 풀어주세요. str() 사용 금지

s = int(input())
a = s
count = 0
while s > 0:
    count +=1
    s = int(s / 10)
    if s == 0:
        break
lst = []
lst2 = []
for i in range(count-1,-1,-1):
    lst.append(10**i)

for i in range(count):
    c = a / int(lst[i])
    lst2.append(int(c))
    a = a % lst[i]
lst2.reverse()
for i in lst2:
    print(i,end='')

    

