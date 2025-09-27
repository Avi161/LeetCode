from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        SIZE = len(nums)
        res = L = start = 0
        zeroIdx = -1

        while start < SIZE and nums[start] != 0:
            start += 1
        if start < SIZE:
            zeroIdx = start
        R = start + 1
        
        while R < SIZE:
            if nums[R] == 0:
                res = max(res, R-L)
                L = zeroIdx + 1
                zeroIdx = R
            R += 1
        res = max(res, R-L)
        return res if zeroIdx != -1 else SIZE-1
Solution().longestSubarray([1,1,0,1])