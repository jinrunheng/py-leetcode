from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        left = 0
        right = 0
        if root.left is not None:
            left = self.rangeSumBST(root.left, low, high)
        if root.right is not None:
            right = self.rangeSumBST(root.right, low, high)
        return root.val + left + right if low <= root.val <= high else left + right
