# 프로그래머스 # 피보나치 수

# 풀이 3 (swap)

def solution(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,(a+b) % 1234567
    return a

# 풀이 2 (DP)

def solution(n):
    DP = [0] * (n+1)
    DP[1] = 1
    for i in range(2, n+1):
        DP[i] = (DP[i-1] + DP[i-2]) % 1234567
    return DP[n]

# 풀이 1 (재귀. 시간초과)
def solution(n):
    def fibo(x):
        if x in (1,2):
            return 1
        return (fibo(x-1) + fibo(x-2)) % 1234567 
    return fibo(n)