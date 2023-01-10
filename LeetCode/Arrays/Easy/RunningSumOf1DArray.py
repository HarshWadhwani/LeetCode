class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        totalSum = 0
        for i in range(len(nums)):
            currentSum = totalSum + nums[i]
            result.append(currentSum)
            totalSum = currentSum

        return result
