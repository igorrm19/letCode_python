
ultimo = None

nums = [1,1,1,2,2,3]
for i in range(len(nums)):
 for j in range(i + 1, len(nums)):
    if nums[i] < nums[j]:
        ultimo = i
        print(i)

