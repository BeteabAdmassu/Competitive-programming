# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj_list = defaultdict(list)

        for course in prerequisites:
            i, j = course
            adj_list[j].append(i)

        def dfs(i):
            if i not in course_prereq:
                course_prereq[i] = set()
                for crs in adj_list[i]:
                    course_prereq[i] |= dfs(crs)
                course_prereq[i].add(i)
            return course_prereq[i]

        course_prereq = {}
        for i in range(numCourses):
            dfs(i)
        
        res = []
        for query in queries:
            i, j = query
            res.append(i in course_prereq[j])
        
        return res