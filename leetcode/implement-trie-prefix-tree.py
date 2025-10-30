class Trie(object):

    def __init__(self):
        self.root = {}

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root

        for letter in word:
            if letter not in curr:
                curr[letter] = {}
            curr = curr[letter]
        
        # mark the end of the word
        curr["*"]=''

        # inserting cat --> {'c': {'a': {'t': {'*': ''}}}}

        # inserting car after --> self.root = {'c': {'a': {'t': {'*': ''}, 'r': {'*': ''}}}}

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curr = self.root

        for letter in word:
            if letter not in curr:
                return False
            curr = curr[letter]

        return "*" in curr

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        
        curr = self.root

        for letter in prefix:
            if letter not in curr:
                return False
            curr = curr[letter]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)