from collections import deque

class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.head_position = [0,0]
        self.food = food[::-1]
        self.food = [[-1, -1]] + self.food
        self.score = 0
        self.occupied = set()
        self.occupied.add((0, 0))
        self.occupied_queue = deque()
        self.occupied_queue.append((0, 0))
        self.m = height
        self.n = width
        

    def move(self, direction: str) -> int:
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        """
        moves = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        
        move = None
        if direction == 'U':
            move = moves[2]
        elif direction == 'D':
            move = moves[3]
        elif direction == 'L':
            move = moves[1]
        else:
            move = moves[0]
            
        # print(self.occupied)
        
        new_head_position = self.head_position[0] + move[0], self.head_position[1] + move[1]
        self.head_position[0] = new_head_position[0]
        self.head_position[1] = new_head_position[1]
        
        print(new_head_position)
        print(self.food)
        print(self.occupied)
        print(self.occupied_queue)
        print()
        print()
        
        
        if len(self.food) != 0 and new_head_position[0] == self.food[-1][0] and new_head_position[1] == self.food[-1][1]:
            self.score += 1
            self.occupied.add((new_head_position[0], new_head_position[1]))
            self.occupied_queue.append((new_head_position[0], new_head_position[1]))
            self.food.pop()
            
            return self.score
            
        elif 0 <= new_head_position[0] < self.m and 0 <= new_head_position[1] < self.n and (new_head_position[0], new_head_position[1]) not in self.occupied and (new_head_position[0] != self.food[-1][0] or new_head_position[1] != self.food[-1][1]):
            self.occupied.add((new_head_position[0], new_head_position[1]))
            self.occupied_queue.append((new_head_position[0], new_head_position[1]))
            obsolete = self.occupied_queue.popleft()
            self.occupied.remove(obsolete)
            return self.score
        
        else:
            return -1
            
        
        

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)