from typing import Set


def largest_sum(nums: Set[int], k : int) -> int:
# checking that every element is actually a natural number        
    for i in nums:
        if i <= 0 or not isinstance(i, int): 
            return "Not a list of unique natural numbers\nHint: 'Natural Numbers start from 1'"
    if not isinstance(nums, Set):
       return "Not a list of unique natural numbers" 
   
   
# return 0 for empty list
    if len(nums) == 0:
        return 0
    elif k > len(nums):
        return "This is going to return an awkward out of range error. k must be less than or equal to n"
    elif k == len(nums):
        return sum(nums)


# assumption that list of numbers satisfies all requirements
    else:
        
        new_nums = list(nums)  # converts nums into list
        largest = [] # stores only the k largest numbers
        
        
# collecting the largest k numbers in the list of numbers
        while len(largest) < k:
            largest.append(new_nums.pop(new_nums.index(max(new_nums)))) # popping the max k numbers
        
        return sum(largest)