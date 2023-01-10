# Approach the array from the last element backwards
# Figure out the possible zeros to be added in beforehand, and manipulate the existing elements accordingly

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        zeroCounter = 0
        lengthOfDups = len(arr) - 1

        for index in range(lengthOfDups + 1):

            if index > lengthOfDups - zeroCounter:
                break

            if arr[index] == 0:
                if index == lengthOfDups - zeroCounter:
                    arr[lengthOfDups] = 0
                    lengthOfDups -= 1
                    break
                zeroCounter += 1

        last = lengthOfDups - zeroCounter

        for index in range(last, -1, -1):
            if arr[index] == 0:
                arr[index + zeroCounter] = 0
                zeroCounter -= 1
                arr[index + zeroCounter] = 0
            else:
                arr[index + zeroCounter] = arr[index]