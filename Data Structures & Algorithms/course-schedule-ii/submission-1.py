class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        reqs = [[] for i in range(numCourses)]
        for course, preReq in prerequisites:
            indegree[course] += 1
            reqs[preReq].append(course)
            
        q = collections.deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        finish, res = 0, []
        while q:
            node = q.popleft()
            res.append(node)
            finish += 1
            for crs in reqs[node]:
                indegree[crs] -= 1
                if indegree[crs] == 0:
                    q.append(crs)
    
        if finish != numCourses:
            return []
        return res