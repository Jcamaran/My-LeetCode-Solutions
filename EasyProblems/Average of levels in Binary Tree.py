# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def averageOfLevels(self, root):
        result= []
        if not root:
            return None
        q = deque([root])
        while q:
            Lsize = len(q)
            level_sum = 0

            for i in range(Lsize):
                node = q.popleft()
                level_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            averageL = float(level_sum) / Lsize
            result.append(averageL)
        return result  
                

                    





                












        
