class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
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


        #     start = i[0]
        #     end = i[len(i) - 1]
        #     added = False
        #     for j in seen:
        #         print(i)
        #         if start >= j[0] and end <= j[len(j) - 1]:
        #             added = True
        #             break
        #         elif start <= j[0] and end >= j[len(j) - 1]:
        #             j[0] = min(start, j[0])
        #             j[1] = max(end, j[len(j) - 1])
        #         elif start in range(j[0], j[len(j) - 1]):
        #             j[1] = end
        #             added = True
        #             break
        #         elif end in range(j[0], j[len(j) - 1]):
        #             j[0] = start
        #             added = True
        #             break

        #     if not added:
        #         seen.append(i)

        # return seen