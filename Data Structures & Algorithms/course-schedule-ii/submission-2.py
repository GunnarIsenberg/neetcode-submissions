class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #We're going to need a hashmap that maps a course ID to a list -> we will populate that list with all pre-requisites. 
        preReqs = {i : [] for i in range(numCourses)}
        for course, preReq in prerequisites:
            preReqs[course].append(preReq)
        
        visited, cycle = set(), set()
        res = []

        def dfs(node):
            if node in cycle:
                return False
            if node in visited:
                return True

            cycle.add(node)
            for req in preReqs[node]:
                if not dfs(req):
                    return False
            cycle.remove(node)
            visited.add(node)
            res.append(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
        

        
        