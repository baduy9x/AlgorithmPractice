class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        current_length = 0
        max_length = 0
        idx = 0
        last_dup_index = -1
        count = {}
        while idx < len(s):
            if s[idx] not in count or count[s[idx]] < last_dup_index:
                count[s[idx]] = idx
                current_length += 1
                max_length = max(max_length, current_length)
            else:
                last_dup_index = count[s[idx]]
                count[s[idx]] = idx
                current_length = idx - last_dup_index
            idx += 1
        return max_length
