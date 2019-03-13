# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        start = ListNode(-1)
        end = start

        while l1 and l2:
            if l1.val > l2.val:
                end.next = ListNode(l2.val)
                l2 = l2.next
            else:
                end.next = ListNode(l1.val)
                l1 = l1.next

            end = end.next

        while l1:
            end.next = ListNode(l1.val)
            l1 = l1.next
            end = end.next

        while l2:
            end.next = ListNode(l2.val)
            l2 = l2.next
            end = end.next

        return start.next
