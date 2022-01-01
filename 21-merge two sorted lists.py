# Definition for single-linked list:
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# iteratively
class Solution:
    def mergeTwo(self, l1, l2):
        curr = dummy = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2

        return dummy.next

