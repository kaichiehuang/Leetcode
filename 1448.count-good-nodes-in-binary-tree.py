#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        currMax = root.val
        count = 0

        def countGoodNodes(root, currMax):
            nonlocal count
            if root.val >= currMax:
                count += 1
            
            currMax = max(currMax, root.val)
            if root.left:
                countGoodNodes(root.left, currMax)
            if root.right:
                countGoodNodes(root.right, currMax)
        
        countGoodNodes(root, currMax)

        return count

# @lc code=end

