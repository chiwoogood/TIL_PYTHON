#주어진 문자열 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력하시오.

#apple
lst = []
apple = list('apple')
for i in apple:
    lst.append(i)
lst.reverse()
lst = ('').join(lst)
print(lst)
