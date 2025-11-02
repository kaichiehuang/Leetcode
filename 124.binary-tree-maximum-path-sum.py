#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float('-inf')

        def find(node):
            nonlocal maxSum
            if not node:
                return 0

            leftSum = max(find(node.left), 0)
            rightSum = max(find(node.right), 0)


            maxSum = max(maxSum, leftSum + rightSum + node.val)

            return node.val + max(leftSum, rightSum)

        find(root)

        return maxSum

# @lc code=end

