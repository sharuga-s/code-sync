import random
class RandomizedSet(object):

    def __init__(self):
        self.rs = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.rs:
            self.rs.append(val)
            return True

        return False

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """

        for i in range(len(self.rs)):
            if self.rs[i] == val:
                self.rs = self.rs[:i] + self.rs[i + 1:]
                return True

        return False
        

    def getRandom(self):
        """
        :rtype: int
        """
        
        return random.choice(self.rs)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()