# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        length=0
        temp = head
        while temp:
            temp = temp.next
            length+=1
        if length%2==0:
            for i in range(int((length/2))):
                head = head.next
            return head
        else:
            for i in range(ceil(length/2)-1):
                head = head.next
            return head