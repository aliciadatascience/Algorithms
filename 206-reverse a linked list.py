# Definition for singly-linked list
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

# for iteratively T:O(n), S:O(1)
class Solution:
    def reverseList(self, head: ListNode):
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

# the best way to think about recursive problems is to break it down into a sub problem
# instead of reverse the entire list, I will reverse the remainder of the linked list

# for recursive T:O(n), S:O(n)
class Solution:
    def reverseList(self, head: ListNode):
        if not head:
            return None

        newHead  = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead