# 프로그래머스 # 행렬의 덧셈

# 풀이 1
def solution(arr1, arr2):
    return [[arr1[i][j] + arr2[i][j] for j in range(len(arr1[0]))] for i in range(len(arr1))]

# 풀이 2 (zip 활용하기)
def solution(arr1, arr2):
    return [[sum(pair) for pair in zip(arr1Row, arr2Row)] for arr1Row, arr2Row in zip(arr1, arr2)]

