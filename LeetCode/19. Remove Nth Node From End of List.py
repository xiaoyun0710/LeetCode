# Given a linked list, remove the n-th node from the end of list and return its head.
#
# Example:
#
# Given linked list: 1->2->3->4->5, and n = 2.
#
# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
#
# Given n will always be valid.
#
# Follow up:
#
# Could you do this in one pass?


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        # remove Nth node from end == remove L-N+1 th node.

        dummy = ListNode(-1)
        dummy.next = head

        a = dummy
        b = dummy

        for i in range(n):
            a = a.next

        while a.next:
            a = a.next
            b = b.next

        if b.next.next:
            b.next = b.next.next
        else:
            b.next = None

        return dummy.next
