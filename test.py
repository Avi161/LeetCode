from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = {} 

        ROWS, COLS = len(matrix), len(matrix[0])
        count = 0

        directions = [[-1,-1],[-1,0],[0,-1]]

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    dp[(r,c)] = 0
                    continue
                else:
                    dp[(r,c)]= 1
                    count += dp[(r,c)]
                    check = 0
                    for dr, dc in directions:
                        if (r+dr, c+dc) in dp and dp[(r+dr,c+dc)] >= 1:
                            check += 1
                    if check == 3:
                        dp[(r,c)] += 1
                        count += dp[(r,c)]
        return count

Solution().countSquares([
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
])