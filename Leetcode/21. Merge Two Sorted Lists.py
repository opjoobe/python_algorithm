# Leetcode # 21. Merge Two Sorted Lists

from typing import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1
        answer = ListNode(0, None)
        now = answer
        while list1 and list2:
            if list1.val <= list2.val:
                now.next = ListNode(list1.val, None)
                now = now.next
                list1 = list1.next
            else:
                now.next = ListNode(list2.val, None)
                now = now.next
                list2 = list2.next
        if list1:
            now.next = list1
        if list2:
            now.next = list2
        return answer.next

    

