# 프로그래머스 # 연속 부분 수열 합의 개수
def solution(elements):
    n = len(elements)
    circular_list = elements.copy()
    results = set(circular_list)
    for length in range(1, n-1):
        for idx in range(n): # for each element, make a consecutive array of length = 'length'
            circular_list[idx] += elements[(idx + length) % n]
            results.add(circular_list[idx])
    return len(results) + 1 # needs to count sum(elements), which is unique (every element is 1 at least)
    # circular_list (length = 1) : [1  ,   2,     4,     7,     9    ]
    # circular_list (length = 2) : [1+2,   2+4,   4+7,   7+9,   9+1  ]
    # circular_list (length = 3) : [1+2+4, 2+4+7, 4+7+9, 7+9+1, 9+1+2]