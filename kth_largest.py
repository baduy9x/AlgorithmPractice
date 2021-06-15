class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums_sorted = sorted(nums, reverse = True)
        return nums_sorted[k]