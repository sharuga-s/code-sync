class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        dependencies = {}

        for i in range(numCourses):
            dependencies[i] = []

        for i in prerequisites:
            dependencies[i[0]].append(i[1])

        donezo = []
        dset = set()

        for i in dependencies:
            if not dependencies[i]:
                donezo.append(i)
                dset.add(i)

        while len(donezo) < numCourses:
            sum_new = False
            for i in prerequisites:
                if i[0] not in dset and self.allIn(dependencies[i[0]], dset):
                    donezo.append(i[0])
                    dset.add(i[0])
                    sum_new = True

            if not sum_new:
                break #must be a cycle

        if len(donezo) != numCourses:
            return []

        return donezo

    def allIn(self, dependents, lst):
        for i in dependents:
            if i not in lst:
                return False

        return True