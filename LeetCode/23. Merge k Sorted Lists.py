# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
#
# Example:
#
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: [ListNode]) -> ListNode:

        # 1. pick out all number
        # 2. sort them
        # 3. init a new ListNode

        start = ListNode(-1)
        end = start

        num = []

        for i in lists:
            while i:
                num.append(i.val)
                i = i.next

        num.sort()

        for j in num:
            end.next = ListNode(j)
            end = end.next

        return start.next
