# 프로그래머스 # 직사각형 별찍기

n, m = map(int, input().strip().split(' '))
print(*['*' * n for _ in range(m)], sep = '\n')