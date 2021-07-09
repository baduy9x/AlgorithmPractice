from collections import deque

class Solution:
    
    def check(self, level_grid):
        m = len(level_grid)
        n = len(level_grid[0])
        for i in range(m):
            for j in range(n):
                if level_grid[i][j] == -1:
                    return True
        return False
    
    def orangesRotting(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        level_grid = [[-1] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    level_grid[i][j] = 0
                elif grid[i][j] == 1:
                    level_grid[i][j] = -1
                else:
                    level_grid[i][j] = -2

        if not self.check(level_grid):
            return 0


        for i in range(m):
            for j in range(n):
                queue = deque()
                seen = set()
                if grid[i][j] == 2 and (i, j) not in seen:
                    level = 0
                    queue.appendleft((i, j, level))
                    level_grid[i][j] = level
                    seen.add((i, j))
                    while queue:
                        x, y, level = queue.pop()
                        # print(x, y, level)
                        for move in ([0, -1], [0, 1], [1, 0], [-1, 0]):
                            neighbor = (x + move[0], y + move[1])
                            if 0 <= neighbor[0] < m and 0 <= neighbor[1] < n and\
                                 grid[neighbor[0]][neighbor[1]] == 1 and neighbor not in seen:
                                queue.appendleft((neighbor[0], neighbor[1], level + 1))
                                if level_grid[neighbor[0]][neighbor[1]] != -1:
                                    level_grid[neighbor[0]][neighbor[1]] = min(level + 1, level_grid[neighbor[0]][neighbor[1]])
                                else:
                                    level_grid[neighbor[0]][neighbor[1]] = level + 1
                                seen.add(neighbor) 

        # print(level_grid)

        if self.check(level_grid):
            return -1
        else:
            return max(max(row) for row in level_grid)
                    

if __name__ == '__main__':
    sol = Solution()

    print(sol.orangesRotting([[2,1,1],[1,1,1],[0,1,2]]))