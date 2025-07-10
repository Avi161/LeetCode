class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        length = len(word)
        path = set()

        def backtrack(r, c, i):
            if i == length:
                return True
            
            if (r >= ROWS or c >= COLS or r < 0 or c < 0 or word[i] != board[r][c] or (r, c) in path):
                return False
            
            path.add((r,c))
            res = (backtrack(r, c + 1, i + 1) or backtrack(r, c - 1, i + 1) or backtrack(r + 1, c, i + 1) or backtrack(r-1, c, i + 1))
            path.remove((r,c))

            return res



        for r in range(len(board)):
            for c in range(len(board[0])):
                if backtrack(r, c, 0):
                    return True
        
        return False