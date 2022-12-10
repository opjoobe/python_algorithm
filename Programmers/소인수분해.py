# 프로그래머스 # 소인수분해

''' 
첫번째 풀이 : 모든 약수를 구하고, 그 중 소수 여부를 확인
어떤 약수가 소수인 경우에만 그 약수와 n // 약수를 answer에 넣고 처리하니까
8012 = 4 * 2003 같은 경우를 처리해주지 못했음.
1,2,4,... 이런식으로 들어가도록 해주어야 했음.
쉬운 문제지만 여기서 상당히 시간이 오래 걸림. 왜 안될까? 하면서 :(
자만하지 말고 분발하자 !
'''
def solution(n):
    answer = {1, n}
    is_prime = [False] * 2 + [True] * (n - 1)
    for num in range(2, int(n ** 0.5) + 1):
        if n % num == 0:
            answer.add(num)
            answer.add(n // num)
        if is_prime[num]:
            for next_num in range(num * num, n + 1, num):
                is_prime[next_num] = False
    return [x for x in sorted(answer) if is_prime[x]]
                
''' 
두번째 풀이 : 소인수분해라는 컨셉에 충실하게 나눌 수 있을때까지 나눠감.
다만 2 이외의 소수는 모두 홀수니까, 처음에 2를 처리해주고
이후엔 홀수만 처리하도록 하니 속도가 매우 빨라짐. 거의 0.00ms에 처리가능.
'''
def solution(n):
    answer = [2] if n % 2 == 0 else []
    while n % 2 == 0:
        n //= 2
    x = 3
    while x <= n:
        if n % x == 0:
            answer.append(x)
            while n % x == 0:
                n //= x
        x += 2
    return answer