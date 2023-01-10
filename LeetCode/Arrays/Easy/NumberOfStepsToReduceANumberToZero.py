from turtle import st


class Solution:
    def numberOfSteps(self, num: int) -> int:
        
        stepCounter = 0

        while num != 0:
            if num % 2 == 1:
                num -= 1
            else:
                num /= 2
            stepCounter += 1
        
        return stepCounter