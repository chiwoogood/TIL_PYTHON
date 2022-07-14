#문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오.
#모음 : a, e, i, o, u 
a = 'apple'
count = 0
vowel = ['a','e','i','o','u']
for i in a:
    if i in vowel:
        count +=1
print(count)

