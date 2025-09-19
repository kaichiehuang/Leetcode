#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        totalLen = len(nums1) + len(nums2)
        halfLen = totalLen // 2

        if (len(B) < len(A)):
            A, B = B, A
        
        l, r = 0, len(A) - 1

        while True:
            aMid = (l+r) // 2
            bMid = halfLen - aMid - 2

            aLeft = A[aMid] if aMid >= 0 else float("-infinity")
            aRight = A[aMid + 1] if aMid + 1 < len(A) else float("infinity")
            bLeft = B[bMid] if bMid >= 0 else float("-infinity")
            bRight = B[bMid + 1] if bMid + 1 < len(B) else float("infinity")

            if aLeft <= bRight and bLeft <= aRight:
                #odd
                if totalLen % 2:
                    return min(aRight, bRight)
                else:
                    return (max(aLeft, bLeft) + min(aRight, bRight) ) / 2
            elif(aLeft > bRight):
                r = aMid - 1
            else:
                l = aMid + 1
        

        
# @lc code=end

