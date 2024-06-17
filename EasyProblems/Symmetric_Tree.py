# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        queue = deque([root])
        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                if node:
                    current_level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    current_level.append(None)
        # Checks it the current level is a palindrome
            if current_level != current_level[::-1]:
                return False
        return True





        
