"""
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.



Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):

    def findNode(self, root, parent, height):
        if root is None:
            return
        if root.val == self.x:
            self.xp = parent
            self.hx = height
        if root.val == self.y:
            self.yp = parent
            self.hy = height
        self.findNode(root.left, root, height + 1)
        self.findNode(root.right, root, height + 1)

    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        self.x = x
        self.y = y
        self.xp = None
        self.yp = None
        self.hx = -1
        self.hy = -2

        self.findNode(root, None, 0)

        return self.xp != self.yp and self.hx == self.hy
