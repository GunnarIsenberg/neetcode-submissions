class TrieNode:
    def __init__(self, char):
        self.nextList = []
        self.charSet = set()
        self.charMap = {}
        self.isTerminal = False
        self.char = char

    def addNext(self, node):
        if node.char in self.charSet:
            return False
        self.charSet.add(node.char)
        self.nextList.append(node)
        self.charMap[node.char] = len(self.nextList) - 1 
        return True
    
    def getNode(self, char):
        if char in self.charSet:
            return self.nextList[self.charMap[char]]
        return None


class PrefixTree:
    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word: str) -> None:
        curNode = self.root
        for ch in word:
            if ch in curNode.charSet:
                curNode = curNode.getNode(ch)
            else:
                newNode = TrieNode(ch)
                curNode.addNext(newNode)
                curNode = newNode
        curNode.isTerminal = True            

    def search(self, word: str) -> bool:
        curNode = self.root
        for ch in word:
            if ch in curNode.charSet:
                curNode = curNode.getNode(ch)
            else:
                return False
        return curNode.isTerminal

    def startsWith(self, prefix: str) -> bool:
        curNode = self.root
        for ch in prefix:
            if ch in curNode.charSet:
                curNode = curNode.getNode(ch)
            else:
                return False
        return True
        
        