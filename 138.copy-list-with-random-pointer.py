#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        

        nodeMap = {None: None}
        curr = head
        
        def getClonedNode(node):
            if node in nodeMap:
                return nodeMap[node]
            else:
                nodeMap[node] = Node(node.val)
                return nodeMap[node]



        while curr:
            cloned = getClonedNode(curr)
            cloned.next = getClonedNode(curr.next)
            cloned.random = getClonedNode(curr.random)
            curr = curr.next

        return nodeMap[head]
        


# @lc code=end

