# Leetcode # 2269. Find the K-Beauty of a Number

from collections import deque
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        checked = {0:False}
        num_list = list(str(num))
        q = deque(num_list[:k])
        now_divisor = int(''.join(q))
        
        if now_divisor != 0 and num % now_divisor == 0:
            k_beauty = 1
            checked[now_divisor] = True
        else:
            k_beauty = 0
            checked[now_divisor] = False
        
        for now_num in num_list[k:]:
            q.popleft()
            q.append(now_num)
            now_divisor = int(''.join(q))
            if now_divisor in checked:
                if checked[now_divisor]:
                    k_beauty += 1
            else:
                if num % now_divisor == 0:
                    k_beauty += 1
                    checked[now_divisor] = True
                else:
                    checked[now_divisor] = False
                    
        return k_beauty
    