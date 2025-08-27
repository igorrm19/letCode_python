

target = 10
nums = [0,5,5]

for i in range(len(nums) - 1):

  atual = nums[i]
  proximo = nums[i + 1]
  soma = atual + proximo

  if soma == target: 
    print(f"o target foi encontrado em {i, i+1}")
    
  else:
    print("o target não foi encontrado")
    