class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return 1

        latestPosition = 0
        newValueFinder = 1

        while newValueFinder < len(nums):
            if nums[newValueFinder] <= nums[latestPosition]:
                newValueFinder += 1
            else:
                latestPosition += 1
                nums[latestPosition] = nums[newValueFinder]

        return latestPosition + 1

            