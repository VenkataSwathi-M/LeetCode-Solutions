# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.diameter = 0
        def height(node):
            if node is None:
                return 0
            lh = height(node.left)
            rh = height(node.right)
            self.diameter = max(self.diameter, lh+rh)
            return 1 + max(lh,rh)
        height(root)
        return self.diameter
        
        
