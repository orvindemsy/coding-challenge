'''

'''

jewels = 'aA'
stones = 'aAAbbbb'


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return len([j for j in stones if j in jewels])


sol = Solution()
print(sol.numJewelsInStones(jewels, stones))
