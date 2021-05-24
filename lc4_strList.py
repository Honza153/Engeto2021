inpt = input("Hello, please write your numbers and press enter to confirm: ")
nums = inpt.split(',')
print(nums)
result = list()

for slv in nums:
    slv1 = slv.strip()
    result.append(slv1)

print(result)

