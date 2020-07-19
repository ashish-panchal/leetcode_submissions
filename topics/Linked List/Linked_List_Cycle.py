# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        if head.next is None:
            return False

        curr = head
        curr2 = head.next

        while curr is not None and curr2 is curr2 is not None:
            curr = curr.next
            if curr2.next:
                curr2 = curr2.next.next
            else:
                return False

            if curr == curr2:
                return True
        return False
