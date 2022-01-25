'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example:
    img...
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
'''

class Solution:

    # DP
    def trap(self, height: List[int]) -> int:
        res = 0
        n = len(height)
        left = [0] * n
        right = [0] * n

        for i in range(0, n):
            left[i] = max(height[i], left[i-1] if i > 0 else 0)
        for j in range(n-1, -1, -1):
            right[j] = max(height[j], right[j+1] if j < n-1 else 0)
        for m in range(1, n-1):
            depth = min(left[m], right[m]) - height[m]
            if depth > 0:
                res += depth
        return res

    # Two Pointers
    def trap2(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        lmax = rmax = 0
        res = 0

        while left <= right:
            if lmax <= rmax:
                if height[left] >= lmax:
                    lmax = height[left]
                res += lmax - height[left]
                left += 1
            else:
                if height[right] >= rmax:
                    rmax = height[right]
                res += rmax - height[right]
                right -= 1
        return res
