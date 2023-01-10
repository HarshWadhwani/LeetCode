class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0

        for i in range(len(accounts)):
            currentSum = 0
            for j in range(len(accounts[i])):
                currentSum += accounts[i][j]
            if maxWealth <= currentSum:
                maxWealth = currentSum
        
        return maxWealth