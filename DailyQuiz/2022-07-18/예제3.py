#두 수를 Input으로 받아 합을 구하는 코드이다.
#코드에서 오류를 찾아 원인을 적고, 수정하세요.

#numbers = input().split()
#print(sum(numbers))

#TypeError numbers의 입력되는 두 수는 정수형으로 형변환을 해줘야함
numbers = input().split()
number = []
for i in numbers:
    number.append(int(i))
print(sum(number))
