'''
https://leetcode.com/problems/course-schedule/
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?



Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
'''



class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [0 for _ in range(numCourses)] 
        graph = [[] for _ in range(numCourses)]
        
        for i, j in prerequisites:
            graph[i].append(j)
        
        def dfs(i):
            if visited[i] == -1:
                return False
            if visited[i] == 1:
                return True
            visited[i] = -1
            
            for j in graph[i]:
                if not dfs(j):
                    return False
            visited[i] = 1
            
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
            
'''        
Explaination:

Graph is represented in a edge list way.
Used visited[] to mark visited node in one searching loop, in order to avoid meet same node in one searching loop.
'''

'''
首先把每门课的prerequisite都放进一个对应index的list里
对于每一次调用dfs函数，里面有两个visited[i]的赋值过程。第一个赋值为-1，如果遇见了-1，那么证明在这个dfs大循环里遇到了之前要上的课，return False
如果没有遇到，则为1，在之后的dfs里，遇到1的证明都行得通
'''

