from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i: [] for i in range(numCourses)}
        for dest, src in prerequisites:
            adj_list[src].append(dest)
        
        # State: 0 = unvisited, 1 = visiting, 2 = visited
        state = [0] * numCourses
        def dfs(course):
            if state[course] == 1:  
                return False
            if state[course] == 2: 
                return True
            state[course] = 1  
            for neighbor in adj_list[course]:
                if not dfs(neighbor):
                    return False
            state[course] = 2 
            return True
        for course in range(numCourses):
            if state[course] == 0:  
                if not dfs(course):
                    return False
        return True