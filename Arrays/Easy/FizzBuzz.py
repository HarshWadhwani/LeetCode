class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        resultList = []
        for i in range(n):
            stringToAppend = str(i + 1)
            
            if ((i + 1) % 3 == 0 ):
                stringToAppend = "Fizz"
            if ((i + 1) % 5 == 0 ):
                stringToAppend = "Buzz"
            if ((i + 1) % 15 == 0 ):
                stringToAppend = "FizzBuzz"

            resultList.append(stringToAppend)

        return resultList

        #it is much cleaner to use a hashmap and map each divisor to its corresponding string. Concatenation is also possible in such a scenario