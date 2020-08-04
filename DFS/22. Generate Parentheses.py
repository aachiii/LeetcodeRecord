'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if not n: return []
        left, right, res = n, n, []
        self.dfs(left, right, res, '')
        return res
        
        
    def dfs(self, left, right, res, path):
        if left > right:
            return    # keep left more than right
        if left == 0 and right == 0:
            res.append(path)  # append path here
            return 
        if left:
            self.dfs(left-1, right, res, path + '(')
        if right:
            self.dfs(left, right-1, res, path + ')')
            
            
'''
A very typical backtracking problem.
A type of find subset problem.

res/path are necessary.

Remember to give dfs func a stop signal.

left first, then right.
'''
