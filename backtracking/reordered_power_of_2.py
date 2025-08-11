# class Solution:
#     def reorderedPowerOf2(self, n: int) -> bool: # type: ignore
#         str_n = str(n)
#         res = []
#         char_list = []

#         def backtrack():
#             nonlocal res
#             if len(char_list) >= len(str_n):
#                 res.append(char_list[:])
#                 return
#             for c in str_n:
#                 if c == "0" and len(char_list) == 0:
#                     break
#                 if c not in char_list:
#                     char_list.append(c)
#                     backtrack()
#                     char_list.pop()
#         backtrack()

# Solution().reorderedPowerOf2(46)

from typing import List
class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:

        x_end = x + k
        y_end = y + k
        sub_grid = [[0]*k for _ in range(k)]
        r, c = 0, 0

        for row in range(x, x_end):
            for col in range(y, y_end):
                sub_grid[r][c] = grid[row][col]
                c += 1
            c = 0
            r += 1
        print(sub_grid)

        for col in range(len(sub_grid)//2):
            for row in range(len(sub_grid)):
                sub_grid[row][col], sub_grid[len(sub_grid)-row-1][col] = sub_grid[len(sub_grid)-row-1][col], sub_grid[row][col]

        print(sub_grid)

Solution().reverseSubmatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]],1,0,3)