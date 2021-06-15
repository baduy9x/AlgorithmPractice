class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        first_missing = 1
        nums_set = set()
        for item in nums:
            nums_set.add(item)
        while first_missing in nums_set:
            first_missing += 1
        return first_missing
