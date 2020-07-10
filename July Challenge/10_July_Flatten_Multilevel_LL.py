"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        """
        - Use stack to store next element before traversing child nodes
        """
        self.stack = []
        if head is None:
            return None
        return self.flat_it(head)

    def flat_it(self, node):
        """
        Corner case:
        1 -> None
        |
        2 -> 5 -> None
        |
        3 -> None
        |
        4 -> None

        During final step :while collecting all nodes if next is null don't assign previous node and keep on assigning
        next node til non-null node gets in the way
        """
        while node.next or node.child:
            if node.child:
                self.stack.append(node.next)
                node.next = node.child
                node.next.prev = node
                node.child = None
                node = node.next
            else:
                node = node.next

        if len(self.stack) > 0:
            node.next = self.stack.pop()

            if node.next is not None:
                node.next.prev = node
                node = node.next
                return self.flat_it(node)
            else:
                return self.flat_it(node)
        else:
            while node.prev is not None:
                node = node.prev

            return node
