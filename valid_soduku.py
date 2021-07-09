from collections import defaultdict


def check_dup(arr):
    hash_map = defaultdict(int)
    for i in arr:
        hash_map[i] += 1
    for item in hash_map:
        if hash_map[item] > 1 and item != ".":
            return True
    return False


class Solution:
    def isValidSudoku(self, board):
        for i in range(9):
            if check_dup(board[i]) or check_dup([row[i] for row in board]):
                return False

        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                mat = []
                mat.extend([board[i][j], board[i + 1][j], board[i + 2][j], board[i][j + 1], board[i+1]
                           [j + 1], board[i+2][j+1], board[i][j + 2], board[i + 1][j + 2], board[i + 2][j + 2]])
                # print(mat)
                if check_dup(mat):
                    # print(i, j)
                    return False
        # print("I went here")
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], [
          "4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
