#1부터 n까지의 합을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.

#sum() 함수 사용 금지



n = int(input())
sum = 0
i = 1
while i <= n:
    sum += i
    i +=1
print(sum)

m = int(input())
j = 1
sum1 = 0
for j in range(m+1):
    sum1 += j
print(sum1)
