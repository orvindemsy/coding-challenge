'''
Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.


For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have 
the greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.


Input: candies = [4,2,1,1,2], extraCandies = 1
Output: [true,false,false,false,false] 
Explanation: There is only 1 extra candy, therefore only kid 1 will have the greatest number of candies among the kids regardless of who takes the extra candy.
'''

# My solution
class Solution():
    def kidsWithCandies(self, candies, extraCandies):
        return [c + extraCandies >= max(candies) for c in candies]

candies = [2,3,5,1,3]
extraCandies = 3

sol = Solution()
print(sol.kidsWithCandies(candies, 3))


# Other solution