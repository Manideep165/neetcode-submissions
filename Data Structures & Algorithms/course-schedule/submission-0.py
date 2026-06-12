class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # Build adjacency list:
        # course -> list of prerequisites
        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # Tracks nodes currently in the DFS path.
        # Used for cycle detection.
        visitSet = set()

        def dfs(crs):

            # If we revisit a course currently
            # in the recursion stack, a cycle exists.
            if crs in visitSet:
                return False

            # No prerequisites left.
            # This course can be completed.
            if preMap[crs] == []:
                return True

            # Mark course as being visited.
            visitSet.add(crs)

            # Check all prerequisites.
            for pre in preMap[crs]:

                # If any prerequisite leads to a cycle,
                # we cannot finish all courses.
                if not dfs(pre):
                    return False

            # Remove from current DFS path.
            visitSet.remove(crs)

            # Memoization:
            # Mark as already processed.
            preMap[crs] = []

            return True

        # Check every course.
        for crs in range(numCourses):

            if not dfs(crs):
                return False

        return True
