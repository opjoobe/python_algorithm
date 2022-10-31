# 프로그래머스 # 햄버거 만들기

def solution(ingredient):
    stack = []
    cnt = 0
    for material in ingredient:
        stack.append(material)
        if material != 1: continue
        while len(stack) >= 4 and stack[-4:] == [1,2,3,1]:
            cnt += 1
            stack.pop()
            stack.pop()
            stack.pop()
            stack.pop()
    return cnt
    