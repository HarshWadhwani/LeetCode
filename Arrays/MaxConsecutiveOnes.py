class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        max = 0

        for index in range(len(nums)):
            if nums[index] == 1 and index == len(nums) - 1:
                if counter + 1 > max:
                    max = counter + 1 
            elif nums[index] == 1:
                counter += 1   
            elif nums[index] == 0:
                if counter > max:
                    max = counter
                counter = 0

        return max