class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        fast = 1

        while (len(nums) > 1) and fast != len(nums):
            if nums[slow] == 0:
                if nums[fast] != 0:
                    nums[slow] = nums[fast]
                    nums[fast] = 0
                    slow += 1
            else:
                slow += 1
            fast += 1