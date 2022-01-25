'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
'''


class Solution:

    # Two Pointer
    # Time Complexity O(n*n), Space O(1)
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                return
            l, r = i+1, len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l<r and nums[l] == nums[l+1]:
                        l += 1
                    while l<r and nums[r] == nums[r-1]:
                        r -= 1

                    l += 1
                    r -= 1
        return res



