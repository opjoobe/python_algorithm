# Leetcode # 2299. Strong Password Checker II

class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        specials = {'!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+'}
        flags = {lambda x: x.islower(), lambda x:x.isupper(), lambda x:x.isdigit(), lambda x: x in specials}
        
        now = password[0]
        for flag in flags:
            if flag(now) == True:
                flags.remove(flag)
                break
        for idx, now in enumerate(password[1:]):
            if now == password[idx]:
                return False
            for flag in flags:
                if flag(now) == True:
                    flags.remove(flag)
                    break
        return len(flags) == 0