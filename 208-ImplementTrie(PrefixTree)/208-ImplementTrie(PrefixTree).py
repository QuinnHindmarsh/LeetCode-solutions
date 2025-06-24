# Last updated: 24/06/2025, 14:30:57
class Node:
    def __init__(self):
        self.childs = {}
        self.end = False

    
class Trie:

    def __init__(self):
        self.root = Node()
        

    def insert(self, word: str) -> None:
        node = self.root

        for i in range(len(word)):
            char = word[i]

            if char not in node.childs:
                node.childs[char] = Node()
                
            node = node.childs[char]

        node.end = True



    def search(self, word: str) -> bool:
        node = self.root

        for i in range(len(word)):
            char = word[i]

            if char not in node.childs:
                return False
                
            node = node.childs[char]
        
        return node.end


    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i in range(len(prefix)):
            char = prefix[i]

            if char not in node.childs:
                return False
                
            node = node.childs[char]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)