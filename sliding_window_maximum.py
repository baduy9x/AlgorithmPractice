from collections import deque

class Solution:

    def maxSlidingWindow(self, nums, k):
        queue = deque()
        max_first = nums[0:k].index(max(nums[0:k]))
        queue.append(max_first)

        for i in range(max_first + 1, k):
            while nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)

        start = k
        result = []
        result.append(nums[queue[0]])

        while start != len(nums):
            while len(queue) != 0 and queue[0] < start - k + 1:
                queue.popleft()
            while len(queue) != 0 and nums[queue[-1]] <= nums[start]:
                queue.pop()
            queue.append(start)
            result.append(nums[queue[0]])
            start += 1

        return result


if __name__ == "__main__":
    print(Solution().maxSlidingWindow([-95,92,-85,59,-59,-14,88,-39,2,92,94,79,78,-58,37,48,63,-91,91,74,-28,39,90,-9,-72,-88,-72,93,38,14,-83,-2,21,4,-75,-65,3,63,100,59,-48,43,35,-49,48,-36,-64,-13,-7,-29,87,34,56,-39,-5,-27,-28,10,-57,100,-43,-98,19,-59,78,-28,-91,67,41,-64,76,5,-58,-89,83,26,-7,-82,-32,-76,86,52,-6,84,20,51,-86,26,46,35,-23,30,-51,54,19,30,27,80,45,22]
, 10))



