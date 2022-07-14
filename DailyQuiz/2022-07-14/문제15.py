#문자열 word가 주어질 때, 해당 문자열에서 a 가 처음으로 등장하는 위치(index)를 출력해주세요.
#a 가 없는 경우에는 -1을 출력해주세요.
#find() index() 메서드 사용 금지

b = 'python'
c = 0
for i in b:
    if i != 'a':
        c += 1
        if c > (len(b)-1):
            c = -1
    elif i == 'a': break
print(c)
    