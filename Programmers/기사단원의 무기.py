# 프로그래머스 # 기사단원의 무기

def solution(number, limit, power):
    divisor = [0, 1] + [2] * (number-1) # initialize the list 'divisor'. every numbers in range (2 ~ number) has at least 2 divisor.
    for num in range(2, int(number ** 0.5) + 1):
        for multiplier in range(num * num, number + 1, num):
            divisor[multiplier] += 2
        if num ** 2 <= number: # num ** 2 is n² of an integer, needs to minus 1, to prevent count same num twice.
            divisor[num ** 2] -= 1
    under_limit_list = list(filter(lambda x : x <= limit, divisor)) # get the list of knights with len(divisors) <= limit.
    return sum(under_limit_list) + (number - (len(under_limit_list) - 1)) * power # get the answer. -1 is necessary because the knight #0 is not the target of this case.