# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return 1
        def check(t1,t2):
            if t1 == None and t2 == None:
                return 1
            if t1 == None or t2 == None:
                return 0
            return (t1.val == t2.val) and check(t1.left,t2.right) and check(t1.right,t2.left)
        return check(root,root)
        
        
        