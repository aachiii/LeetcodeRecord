'''
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.

Example 1:
Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]

Example 2:
Input: s = "3z4"
Output: ["3z4","3Z4"]
'''


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        if not s: return []
        res = []
        self.dfs(res, 0, s, '')
        return res

    def dfs(self, res, index, s, path):
        if len(path) == len(s):
            res.append(path)
            return
        if s[index].isalpha():
            self.dfs(res, index+1, s, path + s[index].upper())
            self.dfs(res, index+1, s, path + s[index].lower())
        else:
            self.dfs(res, index + 1, s, path + s[index])

