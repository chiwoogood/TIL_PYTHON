#아래 코드는 문자열을 입력받아 단어별로 나누는 코드입니다.
#코드에서 오류를 찾아 원인을 적고, 수정하세요.

#words = list(map(int, input().split()))
#print(words)

#map 함수해서 int가아닌 str을 써야한다.
words = list(map(str, input().split()))
print(words)