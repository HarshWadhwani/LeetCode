class Solution:
    
    def removeElement(self, nums: List[int], val: int) -> int:

        left = 0
        right = len(nums) - 1
        result = 0

        while left != len(nums):
            if left < right:
                if nums[left] != val:
                    left += 1
                    result += 1
                    if nums[right] == val:
                        right -= 1

                else:
                    if nums[right] == val:
                        right -= 1

                    else:
                        nums[left] = nums[right]
                        result += 1
                        left += 1
                        right -= 1

            elif left > right:
                    return result  
 
            elif left == right:
                if nums[left] == val :
                    return result 
                else:
                    return result + 1