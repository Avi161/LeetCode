class Solution:
    def maximumSwap(self, num: int) -> int:
        #-----TWO PASS-----#
        # num_arr = [int(_) for _ in str(num)]
        # cmax = -1
        # max_arr = [(0,len(num_arr)-1)]*len(num_arr)
        
        # for i in range(len(num_arr)-1, -1, -1):
        #     if num_arr[i] > cmax:
        #         cmax = num_arr[i]
        #         max_arr[i] = (cmax, i)
        #     else:
        #         max_arr[i] = (cmax, max_arr[i+1][1])
        # print(max_arr)
        
        # for i in range(len(num_arr)):
        #     if max_arr[i][0] > num_arr[i]:
        #         tmp = num_arr[i]
        #         num_arr[i] = max_arr[i][0]
        #         num_arr[max_arr[i][1]] = tmp
        #         break
        
        # return int("".join(str(_) for _ in num_arr))
        
        #-----ONE PASS-----#
        num = list(str(num))
        
        max_digit = "0"
        max_i = -1
        swap_i = swap_j = -1
        
        for i in reversed(range(len(num))):
            # max
            if num[i] > max_digit:
                max_digit = num[i]
                max_i = i
            
            if num[i] < max_digit:
                swap_i, swap_j = i, max_i
        
        num[swap_i], num[swap_j] = num[swap_j], num[swap_i]
        
        return int("".join(num))