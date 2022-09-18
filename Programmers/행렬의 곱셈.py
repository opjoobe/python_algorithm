# 프로그래머스 # 행렬의 곱셈

# 풀이 1
def solution(arr1, arr2):
    # 3 * 2 , 2 * 2    
    a = len(arr1)
    b = len(arr2[0])
    n = len(arr2)
    
    answer = [[0]*b for _ in range(a)]

    for i in range(a):
        for j in range(b):
            answer[i][j] = sum([arr1[i][k] * arr2[k][j] for k in range(n)])
            
    return answer

# 풀이 2 (공부 후 재구성한 풀이))

def solution(arr1, arr2):
    return [[sum([a*b for a,b in zip(row, col)]) for col in zip(*arr2)] for row in arr1] 

# for i in range(a)의 역할을 for row in arr1로 대체하고, 
# for j in range(b)의 역할을 for col in zip(*arr2)로 대체해준다.
# 이렇게 하고 zip(row,col)을 해주면 k라는 변수를 굳이 쓰지 않아도 현재 연산에 필요한 arr1의 row와 arr2의 col에서 하나씩 각각 뽑아올 수 있게 된다.

''' 
두번째 행렬인 arr2이 다음과 같이 [[1,2],[3,4],[5,6]] 라 가정해보자.
-----
|1,2|
|3,4|
|5,6|
-----
이때, arr2를 asterisk로 나타내준 *arr2는 [1,2], [3,4], [5,6]가 된다.
따라서 zip(*arr2) = zip([1,2],[3,4],[5,6]) = ([1,3,5], [2,4,6]) 이 된다.

즉, 어떤 행렬 arr에 대해 zip(*arr)은 row단위로 구성되어 있는 행렬을 col단위로 재구성 해주는 것과 같다 !

'''