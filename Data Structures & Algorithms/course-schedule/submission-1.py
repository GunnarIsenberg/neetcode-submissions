class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReqs = { i : [] for i in range(numCourses)}
        for course, requires in prerequisites:
            preReqs[course].append(requires)
        
        visiting = set()

        def dfs(course):
            if course in visiting:
                return False

            requires = preReqs[course]
            if requires == []:
                return True

            visiting.add(course)
            for req in requires:
                if not dfs(req):
                    return False
            visiting.remove(course)
            preReqs[course] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
            
        