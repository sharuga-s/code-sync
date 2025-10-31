class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        seen = [intervals[0]]
        intervals = intervals[1:]

        for i in intervals:
            prev = seen[-1]
            start = i[0]
            end = i[1]

            if start <= prev[1]:
                prev[1] = max(end, prev[1])
            else:
                seen.append(i)

        return seen