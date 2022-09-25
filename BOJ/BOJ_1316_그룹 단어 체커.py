from sys import stdin
input = stdin.readline
N = int(input())
cnt = 0
for _ in range(N):
    word = input().strip()
    before = word[0]
    flag = True
    L = []
    for now in word[1:]:
        if now != before:
            if before in L:
                flag = False
                break
            L.append(before)
            before = now
    if flag and before not in L: cnt += 1
print(cnt)
