from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        row_sum = ans_row = 0
        for r in range(len(arr)):
            height = arr[r]
            count = 1
            while stack and stack[-1][0] > height:
                h_top, cnt_top = stack.pop()
                row_sum -= h_top*cnt_top
                count += cnt_top
            stack.append((height, count))
            row_sum += height*count
            ans_row += row_sum
        return ans_row%(10**9+7)

print(Solution().sumSubarrayMins([3,2,1,1,2,4]))