class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(9):
            seen = set()

            for i in range(9):
                if board[row][i] == ".":
                    continue
                
                if board[row][i] in seen:
                    return False
                
                seen.add(board[row][i])

        for col in range(9):
            seen = set()

            for j in range(9):
                if board[j][col] == ".":
                    continue
                
                if board[j][col] in seen:
                    return False
                
                seen.add(board[j][col])

        for square in range(9):
            seen = set()

            for i in range(3):
                for j in range(3):
                    val = board[(square // 3) * 3 + i][(square % 3 * 3 + j)]
                    if val == ".":
                        continue
                    
                    if val in seen:
                        return False

                    seen.add(val)

        return True
