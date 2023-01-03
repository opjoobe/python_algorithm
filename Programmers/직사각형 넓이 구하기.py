#프로그래머스 #직사각형 넓이 구하기
def solution(dots):
    dots.sort(key = lambda item: (item[0], item[1]))
    return (dots[-1][0] - dots[0][0]) * (dots[-1][1] - dots[0][1])
