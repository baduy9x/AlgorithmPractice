from collections import defaultdict


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if len(s) == 1 and len(goal) == 1:
            return False

        is_distinct = True
        distinct_map = defaultdict(int)
        for item in s:
            if item in distinct_map:
                is_distinct = False
                break
            else:
                distinct_map[item] += 1

        num_diff = 0
        diff_map = defaultdict(int)



        for i in range(len(s)):
            if s[i] != goal[i]:
                num_diff += 1
                diff_map[i] = s[i]

        if num_diff > 2:
            return False

        if num_diff == 1:
            return False

        if num_diff == 2:
            x, y = diff_map.keys()
            if s[x] == goal[y] and s[y] == goal[x]:
                return True

        if num_diff == 0:
            if is_distinct:
                return False
            return True

        return False
