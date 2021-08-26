


class Solution:
#     def nextPermutation(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         if len(nums) != 1:
#             start = len(nums) - 1
#             while start >= 0:
#                 current = start - 1
#                 while current >= 0 and nums[current] >= nums[start]:
#                     current -= 1
                             
#                 if current >= 0:
#                     nums[current], nums[start] = nums[start], nums[current]
#                     for i in range(current + 1, len(nums) - 1):
#                         for j in range(i + 1, len(nums)):
#                             if nums[i] > nums[j]:
#                                 nums[i], nums[j] = nums[j], nums[i]
                    
                    
                    
#                     break
#                 start -= 1

#             if start < 0:
#                 i = 0
#                 while i != len(nums) // 2 + 1:
#                     nums[i], nums[len(nums) - i - 1] = nums[len(nums) - i - 1], nums[i]
#                     i += 1

                                     
    def nextPermutation(self, nums: List[int]) -> None:
        swap_index = -1
        target_index = -1
        
        for i in range(len(nums) - 1):
            target_item = float("inf")
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    swap_index = i
                    if nums[j] < target_item:
                        target_item = nums[j]
                        target_index = j
        
        if swap_index != -1:
            nums[swap_index], nums[target_index] = nums[target_index], nums[swap_index]
            for i in range(swap_index + 1, len(nums) - 1):
                for j in range(i + 1, len(nums)):
                    if nums[i] > nums[j]:
                        nums[i], nums[j] = nums[j], nums[i]
        else:
            i = 0
            while i != len(nums) // 2:
                nums[i], nums[len(nums) - i - 1] = nums[len(nums) - i - 1], nums[i]
                i += 1
        
        
        
        
        
        
        
        
        