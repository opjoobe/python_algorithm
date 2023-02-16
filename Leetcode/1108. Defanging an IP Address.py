# Leetcode # 1108. Defanging an IP Address

import re

class Solution(object):
    def defangIPaddr(self, address):
        return re.sub(r'\.', '[.]', address)
