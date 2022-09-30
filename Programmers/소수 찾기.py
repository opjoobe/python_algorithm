# 프로그래머스 # 소수 찾기

# 풀이 1 (에라토스테네스의 체로 구현)
def solution(n):
    visited = [True] * 2 + [False] * (n-1)
    sqrtN = int(n ** 0.5)
    for i in range(2, sqrtN + 1):
        if not visited[i]:
            for j in range(i * 2, n+1, i):
                visited[j] = True
    return visited.count(False)

''' 
i*2 가 아니라 i*i 부터 처리해주면 더 빠르게 가능하다.
왜냐하면 i*1은 처리하면 안되고, i*2~i*(i-1)은 이전에 for문을 도는 과정에서 처리되었음.

위에서 sqrtN을 구하는 것도 i*i 가 n보다 커지면 처리하는 의미가 없어지기 때문이었음.
에라토스테네스의 체를 기억하긴 했지만, 이런 디테일한 부분에서 약간 부족했다.

i*2 -> i*i로 수정하면 효율성 테스트케이스 4개 모두 5~10ms 빠르게 개선된다!
'''

# 풀이 2
def solution(n):
    primeSet = set(range(2, n+1))
    for i in range(2, int(n ** 0.5) + 1):
        if i not in primeSet:
            continue
        primeSet -= set(range(i*i, n+1, i))
    return len(primeSet)

'''
다른 사람의 풀이를 보다가 흥미로워서 참고해 구현해보았음.
하지만 속도가 기존 풀이 1보다 현저하게 느림.
효율성 테스트케이스는 무려 3배가량 느리다.
아무래도 숫자 i가 primeSet에 있는지 확인하는 탐색의 시간복잡도가 O(N)이라 그런듯.
위에서 visited[i]로 확인할때는 O(1)이었기에 속도가 더 빨랐던 것으로 추정됨.
'''