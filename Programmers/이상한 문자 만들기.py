# 프로그래머스 # 이상한 문자 만들기

def solution(s):
    return ' '.join([''.join([word[i].lower() if i % 2 else word[i].upper() for i in range(len(word))]) for word in s.split(' ')])

'''
s.split() 으로 하면, 여러 개의 공백이 단일 공백으로 바뀐다.
< 예시> 
s = " try   hello"
s.split() => ['try', 'hello']
s.split(' ') => ['', 'try', '', '', 'hello']

따라서 '각 단어는 하나 이상의 공백문자로 구분되어 있다'는 조건을 충족하기 위해선, 
split(' ')로 해주어야 한다. 
'''