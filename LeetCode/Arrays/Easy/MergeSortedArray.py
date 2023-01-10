class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if n == 0:
            pass
         
        else:

            nums1Pointer = m - 1 
            nums2Pointer = n - 1

            for index in range(len(nums1) - 1, -1, -1):
                if nums1Pointer >= 0 and nums2Pointer >= 0:

                    if nums1[nums1Pointer] >= nums2[nums2Pointer]:
                        nums1[index] = nums1[nums1Pointer]
                        nums1Pointer -= 1

                    else:
                        nums1[index] = nums2[nums2Pointer]
                        nums2Pointer -= 1

                elif nums1Pointer < 0 and nums2Pointer >= 0:
                    nums1[index] = nums2[nums2Pointer]
                    nums2Pointer -= 1

                elif nums2Pointer < 0 and nums1Pointer >= 0:
                    nums1[index] = nums1[nums1Pointer]
                    nums1Pointer -= 1