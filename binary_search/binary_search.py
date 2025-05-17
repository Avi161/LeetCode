# 704. Binary Search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1

        while L <= R:
            mid = (R+L)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                R = mid - 1
            else: 
                L = mid + 1
        return -1