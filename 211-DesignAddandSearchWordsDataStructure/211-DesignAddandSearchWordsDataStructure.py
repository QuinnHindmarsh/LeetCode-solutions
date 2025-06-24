# Last updated: 24/06/2025, 14:49:45
class Node:
    def __init__(self):
        self.childs = {}
        self.end = False


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root

        for i in range(len(word)):
            char = word[i]

            if char not in node.childs:
                node.childs[char] = Node()
                
            node = node.childs[char]

        node.end = True

    def search(self, word: str, i=0, node=None) -> bool:
        if not node:
            node = self.root

        if i == len(word):
            return node.end

        char = word[i]

        if char != '.' and char not in node.childs:
            return False
        
        elif char != '.' and char in node.childs: 
            return self.search(word, i+1, node.childs[char])

        else:
            if not node.childs: 
                return False

            for letter in node.childs:
                child_node = node.childs[letter]
                if self.search(word, i+1, child_node):
                    return True
            return False





# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)