class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        result = 0

        countList = [0] * (max(heights) + 1)

        for index in range(len(heights)):
            countList[heights[index]] += 1

        for index in range(1, len(countList)):
            countList[index] += countList[index - 1]

        for index in range(len(heights)):
            result += (heights[countList[heights[index]]-1] != heights[index])
            countList[heights[index]] -= 1
        
        return result