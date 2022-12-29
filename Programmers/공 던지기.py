#프로그래머스 #공던지기

# sol 1 (first solution)
def solution(numbers, k):
    if len(numbers) % 2 == 0:
        return [num for idx, num in enumerate(numbers) if idx % 2 == 0][(k - 1) % (len(numbers) // 2)]
    left, right = list(), list()
    for idx, num in enumerate(numbers):
        if idx % 2 == 0:
            left.append(num)
        else:
            right.append(num)
    return (left + right)[(k - 1) % len(numbers)]

# sol 2 (2x because its just about 'jump')
def solution(numbers, k):
    return numbers[2 * (k - 1) % len(numbers)]

