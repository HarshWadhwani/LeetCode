from re import L


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        for index in range(len(nums)):
            
            numAtPosition = abs(nums[index]) - 1

            nums[numAtPosition] = -1 * abs(nums[numAtPosition])

        res = []

        for index in range(len(nums)):

            if nums[index] > 0:
                res.append(index + 1)

        return res
