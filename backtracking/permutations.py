from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        length = len(nums)
        sol = []

        def backtrack():
            if len(sol) == length:
                res.append(sol.copy())
                return
            
            for num in nums:
                if num not in sol:
                    sol.append(num)
                    backtrack()
                    sol.pop()
        
        backtrack()

        return res