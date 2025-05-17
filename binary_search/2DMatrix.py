# 74. Search a 2D Matrix

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowS, rowE = 0, len(matrix)-1
        colS, colE = 0, len(matrix[0])-1


        while rowS <= rowE:
            midR = (rowS+rowE)//2
            colS, colE = 0, len(matrix[0])-1
            while colS <= colE:
                midC = (colS+colE)//2
                if matrix[midR][midC] == target:
                    return True
                elif matrix[midR][midC] > target:
                    colE = midC-1
                else:
                    colS = midC+1

            if matrix[midR][midC] > target:
                rowE = midR - 1
            if matrix[midR][midC] < target:
                rowS = midR + 1
        return False