# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        count=0
        while head:
            count+=head.val
            count*=2
            head = head.next
        return int(count/2)