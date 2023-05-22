# Leetcode # 203. Remove Linked List Elements

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        start = ListNode(next=head)
        before = start
        now = start.next
        while now:
            if now.val == val:
                before.next = now.next
            else:
                before = now
            now = now.next
        return start.next