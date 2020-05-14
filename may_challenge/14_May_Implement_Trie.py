"""
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
"""
from collections import defaultdict

class TrieNode():
    def __init__(self):
        self.children = defaultdict()
        self.end_of_word = False

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.get_node()

    def get_node(self):
        return TrieNode()

    # Get index based on the characters
    def get_index(self, ch):
        return ord(ch) - ord('a')

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        root = self.root

        for char in word:
            index = self.get_index(char)

            if index not in root.children:
                root.children[index] = self.get_node()
            root = root.children.get(index)

        root.end_of_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        root = self.root

        for char in word:
            index = self.get_index(char)

            if not root.children[index]:
                return False
            root = root.children[index]

        if root and root.end_of_word:
            return True
        else:
            return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        root = self.root

        for char in prefix:
            index = self.get_index(char)

            if index not in root.children:
                return False
            root = root.children[index]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert("word")
# param_2 = obj.search("word")
# param_3 = obj.startsWith("wo")