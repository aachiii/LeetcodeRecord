'''
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
'''


class Solution:

    # typical DFS question
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        res = []
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index+1, len(nums)):
            self.dfs(nums, i, path+[nums[i]], res)

    # DP, Add the new element to each of previous
    def subsets2(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        res = [[]]
        for i in range(len(nums)):
            for r in range(len(res)):
                res.append(res[r]+[nums[i]])
        return res