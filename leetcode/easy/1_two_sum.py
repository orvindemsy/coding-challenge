'''
20201219
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
https://leetcode.com/problems/two-sum/
'''

import numpy as np


# My own version
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    summ = nums[i] + nums[j]  
                    #print(summ)  
                    if summ == target:
                        first_idx = i
                        second_idx = j

                        return [first_idx, second_idx]
                
        return None


# Other solution
class Solution2():
    def twoSum(self, nums, target):
        seen = {}
        for i, current_num in enumerate(nums):
            remaining = target - current_num
            
            if remaining in seen:
                return [seen[remaining], i]

            seen[current_num] = i

        return [] 




# Run code
nums = [3, 2, 4]
target = 6

sol = Solution2()

# Should return 1, 2
print(sol.twoSum(nums, target))



# def twosum(nums, target):
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             if i != j:
#                 summ = nums[i] + nums[j]  
#                 #print(summ)  
#                 if summ == target:
#                     first_idx = i
#                     second_idx = j

#                     return first_idx, second_idx
                
#     return None, None


# # nums = [2, 7, 11, 15]
# # target = 9


# a, b = twosum(nums, target)

# print(a)
# print(b)