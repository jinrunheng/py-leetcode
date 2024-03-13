# 1261. 在受污染的二叉树中查找元素
# https://leetcode.cn/problems/find-elements-in-a-contaminated-binary-tree/description
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.elements = set()
        if root is None:
            return
        else:
            element_queue = deque()
            root.val = 0
            element_queue.append(root)
            self.elements.add(root.val)
            while len(element_queue) > 0:
                poll = element_queue.popleft()
                if poll.left is not None:
                    poll.left.val = poll.val * 2 + 1
                    self.elements.add(poll.left.val)
                    element_queue.append(poll.left)
                if poll.right is not None:
                    poll.right.val = poll.val * 2 + 2
                    self.elements.add(poll.right.val)
                    element_queue.append(poll.right)

    def find(self, target: int) -> bool:
        return target in self.elements


root = TreeNode(-1)
node1 = TreeNode(-1)
node2 = TreeNode(-1)
node3 = TreeNode(-1)
root.right = node1
node1.left = node2
node2.left = node3
find = FindElements(root)
print(find.find(2))
print(find.find(3))
print(find.find(4))
print(find.find(5))
# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
