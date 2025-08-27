
# somar todos os numeros possiveis

nums = [1,2,3,4,5,6,7,8,9,10,11]

for i in range(len(nums)):
   for j in range(i + 1, len(nums)):
       print(nums[i] + nums[j])

       