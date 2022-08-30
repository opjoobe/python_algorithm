from sys import stdin
input = stdin.readline
N = input().strip()

def getGenerator(n):
    digits = len(n)
    target = int(n)
    mini = target - 9 * digits
    start = mini if mini > 1 else 1
    for now in range(start,target):
        if now + sum([int(x) for x in str(now)]) == target:
            return now
    return 0

M = getGenerator(N)
print(M)
            
