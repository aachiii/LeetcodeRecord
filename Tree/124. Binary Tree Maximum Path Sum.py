'''
https://leetcode.com/problems/binary-tree-maximum-path-sum/

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = float('-inf')
        self.dfs(root)
        return self.ans
    
    def dfs(self, root):
        if not root: return 0
        sum_l = max(0, self.dfs(root.left))
        sum_r = max(0, self.dfs(root.right))
        self.ans = max(self.ans, sum_l + sum_r + root.val)
        return max(sum_l, sum_r) + root.val
'''
Recursive
'''
