#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1


        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            
            # Check which half is sorted
            if nums[l] <= nums[mid]:  # Left half is sorted
                if nums[l] <= target < nums[mid]:  # Target is in left half
                    r = mid - 1
                else:  # Target is in right half
                    l = mid + 1
            else:  # Right half is sorted
                if nums[mid] < target <= nums[r]:  # Target is in right half
                    l = mid + 1
                else:  # Target is in left half
                    r = mid - 1

        return -1




# @lc code=end

