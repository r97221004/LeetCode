# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root, k):
        return self.dfs(root)[k-1]

    def dfs(self, root):

        res = []

        def traversal(current_node):
            if current_node.left is not None:
                traversal(current_node.left)
            res.append(current_node.val)
            if current_node.right is not None:
                traversal(current_node.right)
        traversal(root)
        return res


class Solution:
    def kthSmallest(self, root, k):
        stack = []
        current_node = root

        while current_node or stack:
            while current_node:
                stack.append(current_node)
                current_node = current_node.left

            current_node = stack.pop()
            k -= 1
            if k == 0:
                return current_node.val
            current_node = current_node.right
