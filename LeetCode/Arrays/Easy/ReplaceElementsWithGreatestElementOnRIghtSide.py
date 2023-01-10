class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        max = arr[-1]

        arr[-1] = -1

        for index in range(len(arr) - 2, -1, -1):
            if max < arr[index]: 
                temp = arr[index]
                arr[index] = max
                max = temp
            else:
                arr[index] = max
        
        return arr

