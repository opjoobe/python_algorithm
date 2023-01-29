# Leetcode # 929. Unique Email Addresses

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_email_set = set()
        for email in emails:
            new_local_name = ''
            local_name, domain = email.split('@')
            for letter in local_name:
                if letter == '.': continue
                if letter == '+': break
                new_local_name += letter 
            unique_email_set.add(new_local_name + '@' + domain)               
        return len(unique_email_set)
        
# 60ms (beats 62.2%)
