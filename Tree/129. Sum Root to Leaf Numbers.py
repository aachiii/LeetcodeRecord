'''
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

Example:
      4
    /  \
   9   0
  / \
 5  1

Input: root = [4,9,0,5,1]
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.

'''

import collections
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # DFS recursively
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.dfs(root, 0)
        return self.ans

    def dfs(self, root, i):
        val = i * 10 + root.val
        if not root.left and not root.right:
            self.ans += val
            return
        if root.left:
            self.dfs(root.left, val)
        if root.right:
            self.dfs(root.right, val)
        return

    # BFS with queue
    def sumNumbers2(self, root: TreeNode) -> int:
        deque = collections.deque()
        ans = 0
        if root:
            deque.append(root)
        while deque:
            node = deque.popleft()
            if not node.left and not node.right:
                ans += node.val
            if node.left:
                node.left.val += node.val*10
                deque.append(node.left)
            if node.right:
                node.right.val += node.val*10
                deque.append(node.right)
        return ans

    # DFS with stack
    def sumNumber3(self, root: TreeNode):
        stack = []
        ans = 0
        if root:
            stack.append(root)
        while stack:
            node = stack.popleft()
            if not node.left and not node.right:
                ans += node.val
            if node.left:
                node.left.val += node.val * 10
                stack.append(node.left)
            if node.right:
                node.right.val += node.val * 10
                stack.append(node.right)
        return ans






