class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for index in range(len(nums)):
            if nums[index] < 0:
                nums[index] *= -1

        nums.sort()

        for index in range(len(nums)):
            nums[index] *= nums[index]

        return nums