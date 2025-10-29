#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #by James
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node, minVal, maxVal):
            if not node:
                return True
            
            if not (minVal < node.val < maxVal):
                return False
            
            return validate(node.left, float('-inf'), node.val) and validate(node.right, node.val, float('inf'))
        
        return validate(root, float('-inf'), float('inf'))





# @lc code=end

