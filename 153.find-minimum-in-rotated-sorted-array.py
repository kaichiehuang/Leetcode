#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            mid = (l+r) // 2
            res = min(nums[mid], res)

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        
        return res
# @lc code=end

