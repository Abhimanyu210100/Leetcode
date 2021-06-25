# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q == None:
            return 1
        if p == None or q == None:
            return 0
        if p.val != q.val:
            return 0
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        
        
#         def dfs(p,q):
#             if p == None and q == None:
#                 return
#             if p != None and q == None:
#                 key.append(0)
#                 return
#             if p == None and q != None:
#                 key.append(0)
#                 return
#             if p.val != q.val:
#                 key.append(0)
#                 return
#             dfs(p.left,q.left)
#             dfs(p.right,q.right)
#             if 0 in key:
#                 return
#         key = []
#         if p != None and q != None:
#             dfs(p,q)
#         elif p == None and q == None:
#             return 1
#         else:
#             return 0
#         if 0 in key:
#             return 0
#         else:
#             return 1
        