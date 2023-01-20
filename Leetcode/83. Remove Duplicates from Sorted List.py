# Leetcode # 83. Remove Duplicates from Sorted List

from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        before = head
        while before:
            now = before.next
            while now and now.val == before.val:
                now = now.next
            before.next = now
            before = now
        return head


# 36 ms (beats 96.43%) 