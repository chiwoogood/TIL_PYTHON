#양의 정수 number가 주어질 때, 숫자의 길이를 구하시오. 
#양의 정수number를 문자열로 변경하는 것은 금지입니다. str() 사용 금지

#123

number = 123
count = 0
while number / 10 > 0:
    count +=1
    number = number / 10
    if number < 1:
        break
print(count)







