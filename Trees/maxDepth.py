# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return int(0)
        def bfs(t,temp):
            temp+=1
            if t == None:
                temp-=1
                soln.append(temp)
                return int(0)
            bfs(t.left,temp)
            bfs(t.right,temp)
        
        soln=[]
        temp=0
        bfs(root,temp)
        return max(soln)
        
        # return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))