#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        for index, head in enumerate(lists):
            if head:
                heapq.heappush(minHeap, (head.val, index, head))

        dummy = ListNode()
        head = dummy

        while len(minHeap) > 0:
            minElement = heapq.heappop(minHeap)
            minNode = minElement[2]
            minIndex = minElement[1]
            head.next = minNode
            head = head.next
            if minNode.next:
                heapq.heappush(minHeap, (minNode.next.val, minIndex, minNode.next))
        
        return dummy.next



# @lc code=end

