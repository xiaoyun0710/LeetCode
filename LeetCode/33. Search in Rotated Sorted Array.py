# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# Example 1:
#
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
#
# Example 2:
#
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1


class Solution:
    def search(self, nums: [int], target: int) -> int:
        L = 0
        H = len(nums)

        # 变体二分法
        while L < H:
            M = (L + H) // 2

            if target < nums[0] < nums[M]:  # 左边有序，但目标在右边
                L = M + 1
            elif target >= nums[0] > nums[M]:  # 右边有序，但目标在左边
                H = M
            elif target > nums[M]:  # 右边有序，目标在右边
                L = M + 1
            elif target < nums[M]:  # 左边有序，目标在左边
                H = M
            else:  # target = nums[M]
                return M
        return -1
