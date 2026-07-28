class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        #first make dependencies list

        dependencies = {}

        for i in range(numCourses):
            if i not in dependencies:
                dependencies[i] = []

        for i in prerequisites:
            dependencies[i[0]].append(i[1])

        #now basically, if there's no cycle, we can finish!

        is_cycle = False

        states = {}
        for i in range(numCourses):
            states[i] = 0

        for i in dependencies:
            if self.visit(i, states, dependencies):
                is_cycle = True
                break

        return not is_cycle

    def visit(self, node, states, dependencies):
        
        if states[node] == 2:
            return False

        if states[node] == 1:
            return True

        states[node] = 1

        for i in dependencies[node]:
            if self.visit(i, states, dependencies):
                return True

        states[node] = 2
        return False