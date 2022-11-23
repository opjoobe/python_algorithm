# 프로그래머스 # 가장 큰 수 # 레벨 2

def solution(numbers):
    return ''.join(sorted(map(str, numbers), key = lambda x: x*4, reverse = True)) if max(numbers) != 0 else '0'

'''
옛날에  * 4 를 한 다음에 한자리씩 비교하는 코드를 짰었는데,
몇 달이 경과한 오늘 이 문제를 문득 보고 혹시나 하는 마음에 풀었더니 거의 한 번에 성공했다. 
numbers의 모든 원소가 0일 수도 있겠다는 것은 나중에 떠올리긴 했다....!
'''