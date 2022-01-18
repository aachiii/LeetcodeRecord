'''
Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).

Example 1:

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
'''


import heapq


class Solution:

    # time complexity O(n^2 * logk)
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        maxHeap = []
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                heapq.heappush(maxHeap, -matrix[i][j])
                if len(maxHeap) > k:
                    heapq.heappop(maxHeap)
        return -heapq.heappop(maxHeap)
    # maxheap is ascending

    #time complexity O(nloga)
    def kthSmallest2(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        #each time count less or equal
        def countLessOrEqual(x):
            cnt = 0
            c = n - 1
            for r in range(n):
                while c >= 0 and matrix[r][c] > x:
                    c -= 1
                    cnt += (c+1)
            return cnt

        left, right = matrix[0][0], matrix[-1][-1]

        ans = -1
        while left <= right:
            mid = (left+right)//2
            if countLessOrEqual(mid) >= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans

'''
* heapq complexity logk

method 2: So we find the value by binary search. Narrowing the ans range with left and right. Then find how many element is smaller.
    use a pointer to countLessOrEqual

'''







