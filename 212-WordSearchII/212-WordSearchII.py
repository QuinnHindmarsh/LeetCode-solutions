# Last updated: 24/06/2025, 16:04:31
class Node:
    def __init__(self):
        self.childs = {}
        self.word = None

    
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

        node.word = word



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

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.trie = Trie()
        self.root = self.trie.root
        ans = set()
        self.board = board
        self.n = len(board)
        self.m = len(board[0])

        for word in words:
            self.trie.insert(word)

        for i in range(self.n):
            for j in range(self.m):
                char = self.board[i][j]
                if char in self.root.childs:
                    found_words = self.dfs(self.root.childs[char],i,j)
                    for word in found_words:
                        ans.add(word)
        return list(ans)

    def dfs(self, node, i, j):
        temp = self.board[i][j]
        self.board[i][j] = '#'
        cords = [[1,0], [-1,0], [0,1], [0,-1]]
        words = set()

        if node.word:
            words.add(node.word)

        for x,y in cords:
            a = x + i
            b = j + y
            if self.valid_cords(a,b) and self.board[a][b] in node.childs:
                new_words = self.dfs(node.childs[self.board[a][b]],a,b)

                for word in new_words:
                    if word: 
                        words.add(word)

        self.board[i][j] = temp
        return words


    def valid_cords(self,i,j):
        return 0 <= i < self.n and 0 <= j < self.m

        