# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 時間複雜度: O(log(n))
# 空間複雜度: O(1)
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        current_node = root
        while current_node:
            if p.val > current_node.val and q.val > current_node.val:
                current_node = current_node.right
            elif p.val < current_node.val and q.val < current_node.val:
                current_node = current_node.left
            else:
                return current_node
