# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currentNode = head
        resultNode = head
        nodeCounter = 0

        while currentNode.next != None:
            
            currentNode = currentNode.next
            nodeCounter += 1

        jumps = 0
        if nodeCounter % 2 == 0:
            jumps = nodeCounter / 2
        else:
            jumps = ((nodeCounter + 1) / 2)
            
            
        for x in range(int(jumps)):
            resultNode = resultNode.next

        return resultNode