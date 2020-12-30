'''
20201220

You are given an m x n integer grid accounts where accounts[i][j] is the amount of money 
the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

A customer's wealth is the amount of money they have in all their bank accounts. 
The richest customer is the customer that has the maximum wealth.

Example:
Input: accounts = [[1,5],[7,3],[3,5]]
Output: 10
Explanation: 
1st customer has wealth = 6
2nd customer has wealth = 10 
3rd customer has wealth = 8
The 2nd customer is the richest with a wealth of 10.

Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6 each, so return 6.
'''

# My submission
import numpy as np

class Solution():
    def maximumWealth(self, accounts):
        return max(np.sum(accounts, axis=1))

accounts = np.array([[1, 5],
                     [7, 3],
                     [3, 5]])

sol = Solution()

# Other solution
class Solution2():
    def maximumWealth(self, accounts):
        return max(map(sum, accounts))

sol2 = Solution2()

print(sol2.maximumWealth(accounts))