

target = 10
nums = [0,5,5]

for i in range(len(nums)): # numero fixo
  for j in range(i + 1,len(nums)): # numero apos ele
    print(nums[i], nums[j]) #
    soma = nums[i] + nums[j] # 
    if soma == target: #
        print([i,j]) #
    else:
        print([]) #
    
  
    