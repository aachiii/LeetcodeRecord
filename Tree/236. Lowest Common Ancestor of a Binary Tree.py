'''
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example:
           3
         /   \
        5     1
       / \   / \
      6  2  0  8
        / \
       7  4

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # my solution. dfs and use a dict to note down the ancestor
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        hashmap = {}
        found_p, found_q = False, False

        def dfs(node, found_p, found_q):
            if not node: return
            if node.val == p.val:
                found_p = True
            if node.val == q.val:
                found_q = True
            if found_p and found_q:
                return
            if node.left:
                hashmap[node.left] = node
                dfs(node.left, found_p, found_q)
            if node.right:
                hashmap[node.right] = node
                dfs(node.right, found_p, found_q)

        dfs(root, found_p, found_q)

        q_list = [root.val]
        p_list = [root.val]
        while q in hashmap:
            q_list.append(q)
            q = hashmap[q]
        while p in hashmap:
            if p in q_list:
                return p
            else:
                p_list.append(p)
                p = hashmap[p]
        return root

    # recursive ...smart
    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if p == root or q == root:
            return root
        left = self.lowestCommonAncestor1(root.left, p, q)
        right = self.lowestCommonAncestor1(root.right, p, q)

        if left and right:
            return root
        if not left:
            return right
        if not right:
            return left

