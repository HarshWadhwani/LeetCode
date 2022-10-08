class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        uniqueNums = list(set(nums))

        if len(uniqueNums) < 3:
            return max(uniqueNums)

        result = 0
        tries = 3

        while tries != 0:
            result = uniqueNums.pop(uniqueNums.index(max(uniqueNums)))
            tries -= 1

        return result