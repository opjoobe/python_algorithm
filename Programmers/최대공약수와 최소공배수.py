# 프로그래머스 # 최대공약수와 최소공배수
from math import gcd
def solution(n, m):
    return [gcd(n,m), (n // gcd(n,m)) * m ]