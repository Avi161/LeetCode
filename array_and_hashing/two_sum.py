class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_idx = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in num_idx:
                return [num_idx[complement], i]
            else:
                num_idx[num] = i
        