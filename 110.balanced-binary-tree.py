#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def height(node):
            if not node:
                return 0
            
            l = height(node.left)
            if l == -1:  # Left subtree is unbalanced, stop early
                return -1
            
            r = height(node.right)
            if r == -1:  # Right subtree is unbalanced, stop early
                return -1

            # Check if current node is unbalanced
            if abs(l - r) > 1:
                return -1
            
            return 1 + max(l, r)

        return height(root) != -1



# @lc code=end

