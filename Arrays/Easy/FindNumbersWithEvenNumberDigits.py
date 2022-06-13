class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        counter = 0
        for number in nums:

            numberToString = str(number)
            digitCount = len(numberToString)
            if digitCount % 2 == 0:
                counter += 1


        return counter