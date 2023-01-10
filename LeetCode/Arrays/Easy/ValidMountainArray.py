class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        if arr == [] or len(arr) == 1 or arr[1] <= arr[0]:
            return False

        increasing = True

        for index in range(1, len(arr)):
            if increasing:
                if arr[index] == arr[index - 1]:
                    return False
                elif arr[index] < arr[index - 1]:
                    increasing = False
            else:
                if arr[index] >= arr[index - 1]:
                    return False
        
        return not increasing
