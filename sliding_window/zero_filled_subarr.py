from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        L = R = 0
        count = 0

        while R < len(nums):
            if nums[L] != 0:
                L += 1
                R += 1
            else:
                while R < len(nums) and nums[R] == 0:
                    R += 1
                count += 2**(R-L)-1
                L = R
        return count

Solution().zeroFilledSubarray([0,0,0,2,0,0])