nums = [8, 88, 16, 16, 44, 95]

count = 0
prev = nums[0]
next = nums[2]
i = 1
while i <= len(nums)-2:
    if nums[i] == nums[i+1]:
        prev = nums[i-1]
        while i <= len(nums)-2 and nums[i] == nums[i+1]:
            i += 1
            nxt = nums[i+1]

    if (nums[i] < prev and nums[i] < nxt) or (nums[i] > prev and nums[i] > nxt):
        print("Prev: ",prev," Num: ",nums[i],"Next: ",nxt)
        count += 1
    
    i += 1
print(count)