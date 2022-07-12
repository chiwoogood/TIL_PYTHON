#1부터 n까지의 곱을 구하여 출력하는 코드를 1) while 문 2) for 문으로 각각 작성하시오.

n = int(input())
mul = 1
i = 1
while i <= n:
    mul *= i
    i += 1
print(mul)

m = int(input())
mul1 = 1
for j in range(m):
    j +=1
    mul1 *= j
print(mul1)