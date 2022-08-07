# sorted, sorted reverse= True, len, max, min
from cmath import sqrt

sum = 0
nums = list(range(101))
print(max(nums))
print(min(nums))
print(sorted(nums)) # Organizar < a >
print(sorted(nums, reverse=True))
print(len(nums))
for x in nums: 
    if x % 10 == 0: 
        sum += x
print(sqrt(sum))