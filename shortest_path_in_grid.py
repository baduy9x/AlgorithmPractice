from collections import deque

class Solution:
    def shortestPath(self, grid, k: int) -> int:
        queue = deque()
        seen = set()
        
        m = len(grid)
        n = len(grid[0])
        
        queue.append((0, 0, k, 0))
        seen.add((0,0))
        moves = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        
        mat_cost = [[0] * n for _ in range(m)]
        mat_remain = [[0] * n for _ in range(m)]
        mat_remain[0][0] = k


        candidates = []
        
        while queue:
            x, y, remain, cost = queue.popleft()
            
            if remain < 0:
                continue
            
            if x == m - 1 and y == n - 1 and remain >= 0:
                candidates.append(cost)
            
            
            for mov in moves:
                current_x, current_y = x + mov[0], y + mov[1]
                current_cost = cost + 1
                
                if 0 <= current_x < m and 0 <= current_y < n and (current_x, current_y) not in seen and grid[current_x][current_y] == 0:
                        queue.append((current_x, current_y, remain, current_cost))
                        seen.add((current_x, current_y))
                        mat_cost[current_x][current_y] = current_cost
                        mat_remain[current_x][current_y] = remain

            for mov in moves:
                current_x, current_y = x + mov[0], y + mov[1]
                current_cost = cost + 1
                if 0 <= current_x < m and 0 <= current_y < n and (current_x, current_y) not in seen and grid[current_x][current_y] == 1 and remain > 0:
                    queue.append((current_x, current_y, remain - 1, current_cost))
                    seen.add((current_x, current_y))
                    mat_cost[current_x][current_y] = current_cost
                    mat_remain[current_x][current_y] = remain - 1
        # for item in mat_cost:
        #     print(item)

        # print()

        # for item in mat_remain:
        #     print(item)

        if len(candidates) > 0:
            return min(candidates)
        
        return -1

if __name__ == '__main__':
    grid = [[0,0,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,0],[0,1,0,0,0,0,0,0,0,0],[0,1,0,1,1,1,1,1,1,1],[0,1,0,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1,1,0],[0,1,0,0,0,0,0,0,0,0],[0,1,0,1,1,1,1,1,1,1],[0,1,0,1,1,1,1,0,0,0],[0,1,0,0,0,0,0,0,1,0],[0,1,1,1,1,1,1,0,1,0],[0,0,0,0,0,0,0,0,1,0]]
    for item in grid:
        print(item)
    print()
    sol = Solution()
    print(sol.shortestPath(grid, 1))