# 프로그래머스 # 다항식 더하기
def solution(polynomial):
    variable, constant = 0, 0
    answer = []
    for monomial in polynomial.split(' + '):
        if monomial.isdigit():
            constant += int(monomial)
        else:
            if monomial[0] == 'x': monomial = '1x'
            variable += int(monomial[:-1])
    if variable != 0 : answer.append(str(variable) + 'x' if variable != 1 else 'x') # '1x' -> 'x' !!
    if constant != 0 : answer.append(str(constant))
    return answer[0] if len(answer) == 1 else ' + '.join(answer)