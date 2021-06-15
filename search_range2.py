class Solution:
    def searchRange(self, nums, target):
        
        if len(nums) == 0:
            return [-1, -1]


        left = 0
        right = len(nums) - 1
        find_idx = -1
        while left < right:
            mid = (left + right) // 2 + 1
            if nums[mid] == target:
                find_idx = mid
                break
            elif nums[mid] > target:
                right = mid
            else:
                left = mid
            