'''
A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros.
For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.

Given a string n that represents a positive decimal integer, 
return the minimum number of positive deci-binary numbers needed so that they sum up to n.

Example 1:

Input: n = "32"
Output: 3
Explanation: 10 + 11 + 11 = 32

Example 2:

Input: n = "82734"
Output: 8
'''


class Solution():
    def minPartitions(self, n: str) -> int:
        min_partition = 0

        # Iterate until n is zero
        while n != 0:
            #print('current n:', n)

            # Define the deci-binary number as substractor
            num = [0 if i == '0' else 1 for i in str(n)]
            num = int("".join(map(str, num)))
            #print('current num:', num)

            # Define the lowest number in current n as multiplier of substrator
            lowest = min([int(i) for i in str(n) if i != '0'])
            #print('current lowest:', lowest)

            # Substract n by num*lowest
            n = int(n) - num*lowest

            # Add current lowest to min_part
            min_partition += lowest

        return min_partition


sol = Solution()

print(sol.minPartitions(27346209830709182346))
