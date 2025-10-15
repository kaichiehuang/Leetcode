#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def height(node):
            nonlocal diameter
            if not node:
                return 0

            leftH = height(node.left)
            rightH = height(node.right)

            diameter = max(diameter, leftH + rightH)

            return 1 + max(leftH, rightH)

        height(root)

        return diameter
        
# @lc code=end

