class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        for k in prerequisites:
            if k[::-1] in prerequisites:
                return False
        return True