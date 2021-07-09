from collections import deque

class Solution:
    
    def check(self, grid):
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return True
        return False
    
    def orangesRotting(self, grid) -> int:
        if not self.check(grid):
            return 0
        queue = deque()
        seen = set()
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2 and (i, j) not in seen:
                    level = 0
                    queue.appendleft((i, j, level))
                    seen.add((i, j))
                    num_minute = 0
                    while queue:
                        current = queue.pop()

                        for move in ([0, -1], [0, 1], [1, 0], [-1, 0]):
                            neighbor = (current[0] + move[0], current[1] + move[1])
                            if 0 <= neighbor[0] < m and 0 <= neighbor[1] < n and grid[neighbor[0]][neighbor[1]] == 1 and neighbor not in seen:
                                queue.appendleft(neighbor, level + 1)
                                seen.add(neighbor)
                                grid[neighbor[0]][neighbor[1]] = 2    
                         
                    print(num_minute)
                    
                    if max_num_minute < num_minute:
                        max_num_minute = num_minute
        if self.check(grid):
            return -1
        else:
            return max_num_minute
                    

if __name__ == '__main__':
    sol = Solution()

    print(sol.orangesRotting([[2,1,1],[1,1,1],[0,1,2]]))