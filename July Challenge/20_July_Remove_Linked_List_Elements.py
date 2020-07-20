# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return None

        self.head = head

        while self.head:
            if self.head.val == val:
                self.head = self.head.next
            else:
                break

        curr = self.head

        while curr != None:
            if curr.next != None:
                if curr.next.val == val:
                    temp = curr.next.next
                    curr.next.next = None
                    curr.next = temp
                else:
                    curr = curr.next
            else:
                break

        return self.head
