"""
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]



Constraints:

1 <= preorder.length <= 100
1 <= preorder[i] <= 10^8
The values of preorder are distinct.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        return self.construct_bst(preorder)

    def construct_bst(self, preorder):
        if len(preorder) == 0:
            return None

        root = TreeNode(preorder[0])

        left_preorder = []
        right_preorder = []

        for i in range(1, len(preorder)):
            if preorder[i] < root.val:
                left_preorder.append(preorder[i])
            else:
                right_preorder.append(preorder[i])

        left = self.construct_bst(left_preorder)
        right = self.construct_bst(right_preorder)

        root.left = left
        root.right = right

        return root