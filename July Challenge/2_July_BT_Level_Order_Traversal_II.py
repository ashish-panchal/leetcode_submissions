# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        queue = []
        temp = []
        result = []

        def populate_queue (items):
            for item in items:
                queue.append(item)

        def populate_result(items):
            values = []
            for item in items:
                values.append(item.val)
            result.append(values)
            # print result

        queue.append(root)
        populate_result(queue)
        while len(queue) != 0:
            node = queue.pop(0)

            if node.left is not None:
                temp.append(node.left)

            if node.right is not None:
                temp.append(node.right)

            if len(queue) == 0 and len(temp) > 0:
                populate_queue(temp)
                populate_result(temp)
                del temp[:]
        return result[::-1]