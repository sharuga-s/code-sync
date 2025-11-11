class UndergroundSystem(object):

    def __init__(self):
        self.tabs = {}
        self.routeCounts = {}

    def checkIn(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        self.tabs[id] = [stationName, t]
        

    def checkOut(self, id, stationName, t):
        """
        :type id: int
        :type stationName: str
        :type t: int
        :rtype: None
        """
        if (self.tabs[id][0], stationName) not in self.routeCounts:
            self.routeCounts[(self.tabs[id][0], stationName)] = [0.0, 0.0]

        self.routeCounts[(self.tabs[id][0], stationName)][0] += t - self.tabs[id][1]
        self.routeCounts[(self.tabs[id][0], stationName)][1] += 1

        del self.tabs[id]

    def getAverageTime(self, startStation, endStation):
        """
        :type startStation: str
        :type endStation: str
        :rtype: float
        """

        return self.routeCounts[(startStation, endStation)][0] / self.routeCounts[(startStation, endStation)][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)