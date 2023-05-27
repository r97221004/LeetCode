# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root):

        result = self.dfs(root)

        for i in range(1, len(result)):
            if result[i] <= result[i - 1]:
                return False

        return True

    def dfs(self, root):
        # in order DFS
        result = []

        def traversal(current_node):
            if current_node.left is not None:
                traversal(current_node.left)
            result.append(current_node.val)
            if current_node.right is not None:
                traversal(current_node.right)
        traversal(root)
        return result
