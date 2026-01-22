#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #key: Inorder gives sorted order
        counter = 0
        result = None

        def inorder(node):
            nonlocal counter, result
            if not node:
                return
            
            inorder(node.left)
            counter += 1
            if counter == k:
                result = node.val
                return
            inorder(node.right)

        inorder(root)

        return result



# @lc code=end

