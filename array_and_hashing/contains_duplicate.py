class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = set()

        for num in nums:
            if num in num_set:
                return True
            else:
                num_set.add(num)
        
        return False