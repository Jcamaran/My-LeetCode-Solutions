# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        if not root:
            return None
        q = deque([root])

        while q:
            current_node = q.popleft()
            
            current_node.left,current_node.right = current_node.right, current_node.left
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
        return root
    
