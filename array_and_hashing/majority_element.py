res = majority = 0

nums = [1, 2, 2, 3, 4]
for n in nums:
    if majority == 0:
        res = n
    
    majority += 1 if n == res else -1

print(res)