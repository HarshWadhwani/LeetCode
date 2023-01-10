from operator import truediv


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        trackerDict = {"double": [],
                        "half": []}

        for index in range(len(arr)):
            if (arr[index] not in trackerDict["double"]) and (arr[index] not in trackerDict["half"]):
                
                trackerDict["double"].append(arr[index] * 2)
                
                if arr[index] % 2 == 0:
                    trackerDict["half"].append(int(arr[index] / 2))
                
            else:
                return True
            
        return False
                    
            