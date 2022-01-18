'''
Given an array of positive integers nums and a positive integer target,
return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target.
If there is no such subarray, return 0 instead.

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
'''


# greater than or equal to target
class Solution:
    # two pointer O(n)
    def minSubArrayLen(self, s: int, nums: list[int]):
        ans = float('inf')
        left = 0
        sums = 0
        # two pointer, left and i
        for i in range(len(nums)):
            sums += nums[i]
            while sums >= s:
                ans = min(ans, i - left + 1)
                sums -= nums[left]
                left += 1
        return ans if ans != float('inf') else 0

    # better brute force O(n^2) -timeout-
    def minSubArrayLen2(self, s: int, nums: list[int]):
        ans = float('inf')
        if not s:
            return []
        sums = []
        if len(nums) > 0:
            sums.append(nums[0])
            for i in range(1, len(nums)):
                sums.append(nums[i]+sums[i-1])
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                ss = sums[j] - sums[i] + nums[i]
                if ss >= s:
                    ans = min(ans, j - i + 1)
        return ans if ans != float('inf') else 0

'''
can also use binary search with method 2
'''