# Leetcode # 2. Add Two Numbers

from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution for this problem.
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answer = now = ListNode()
        adder = 0

        # add two values from l1 & l2
        while l1 is not None and l2 is not None:
            adder, now_val = divmod(l1.val + l2.val + adder, 10)
            now.next = ListNode(val=now_val)
            now = now.next
            l1, l2 = l1.next, l2.next
        if l1 is not None:
            rest = l1
        elif l2 is not None:
            rest = l2
        else:
            rest = None

        # manage the rest with adder
        while adder != 0 and rest is not None:
            adder, now_val = divmod(rest.val + adder, 10)
            now.next = ListNode(val=now_val)
            now = now.next
            rest = rest.next
    
        if rest is not None:
            now.next = rest
        elif adder != 0:
            now.next = ListNode(val=1)

        return answer.next

# 62ms (beats 89.90%)