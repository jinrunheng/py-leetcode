# https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root


# test
# 构建测试用例的树结构
#      3
#     / \
#    5   1
#   / \ / \
#  6  2 0  8
#    / \
#   7   4
root = TreeNode(3)


def insert(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root


root = insert(root, 5)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 2)
root = insert(root, 0)
root = insert(root, 8)
root = insert(root, 7)
root = insert(root, 4)

p = root.left  # 5
q = root.right.right.right  # 8
solution = Solution()
lca = solution.lowestCommonAncestor(root, p, q)
print("最近的公共节点值:", lca.val)  # 3
