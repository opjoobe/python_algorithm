# 프로그래머스 # 최소직사각형

# 풀이 1
def solution(sizes):
    big, small = 0, 0
    for size in sizes:
        small = max(min(size), small)
        big = max(max(size), big)
    return big * small

# 풀이 2 (한 줄 풀이))
def solution(sizes):
    return max(max(size) for size in sizes) * max(min(size) for size in sizes)