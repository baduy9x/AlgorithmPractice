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

        if find_idx == -1:
            return [-1, -1]
        else:
            start = find_idx
            end = find_idx
            while start != 0 and nums[start - 1] == target:
                start -= 1
            
            while end != len(nums) - 1 and nums[end + 1] == target:
                end += 1
            
            return [start, end]
            
            
        
if __name__ == "__main__":
    print(Solution().searchRange([5,7,7,8,8,10], 8))