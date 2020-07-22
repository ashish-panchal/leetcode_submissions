# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        self.level = []
        self.temp = []
        self.result = []

        # Direction left -> right is 0 and right -> left is 1
        self.direction = 1
        self.level.append(root)
        self.result.append([root.val])

        while len(self.level) != 0:
            if self.direction == 1:
                node = self.level.pop()

                if node.right:
                    self.temp.append(node.right)

                if node.left:
                    self.temp.append(node.left)

                if len(self.level) == 0 and len(self.temp) != 0:
                    for x in self.temp:
                        self.level.append(x)

                    self.direction = 0
                    self.result.append([self.level[x].val for x in range(len(self.level))])
                    self.temp = []
            else:
                node = self.level.pop()

                if node.left:
                    self.temp.append(node.left)

                if node.right:
                    self.temp.append(node.right)

                if len(self.level) == 0 and len(self.temp) != 0:
                    for x in self.temp:
                        self.level.append(x)

                    self.direction = 1
                    self.result.append([self.level[x].val for x in range(len(self.level))])
                    self.temp = []

        return self.result
