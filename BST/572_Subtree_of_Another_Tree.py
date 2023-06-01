# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root, subRoot) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.SameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def SameTree(self, p, q):
        if not p and not q:
            return True

        if p and q and p.val == q.val:
            return self.SameTree(p.left, q.left) and self.SameTree(p.right, q.right)
        return False
