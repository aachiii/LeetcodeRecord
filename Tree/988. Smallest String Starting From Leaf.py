'''
You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.

Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

As a reminder, any shorter prefix of a string is lexicographically smaller.

For example, "ab" is lexicographically smaller than "aba".
A leaf of a node is a node that has no children.

Example:
            z
          /   \
         b    d
        / \  / \
       b  d a  c
Input: root = [25,1,3,1,3,0,2]
Output: "adz"
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    #DFS
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.ans = '~' # ASKII '~' > 'z'
        self.dfs(root, '')
        return self.ans

    def dfs(self, root, path):
        if not root.left and not root.right: #find a leaf
            self.ans = min(self.ans, chr(root.val + 97) + path)
            return
        if root.left:
            self.dfs(root.left, chr(root.val + 97) + path)
        if root.right:
            self.dfs(root.right, chr(root.val + 97) + path)
        return