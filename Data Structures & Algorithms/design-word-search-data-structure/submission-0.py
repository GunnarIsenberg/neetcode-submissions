class TrieNode:
    def __init__(self, char):
        self.char = char
        self.charMap = {}
        self.charSet = set()
        self.nextList = []
        self.isTerminal = False
    
    def getNode(self, char):
        if char in self.charSet:
            return self.charMap[char]
    
    def addNext(self, char):
        if char in self.charSet:
            return self.charMap[char]
        newNode = TrieNode(char)
        self.charSet.add(char)
        self.nextList.append(newNode)
        self.charMap[char] = newNode
        return newNode

class WordDictionary:

    def __init__(self):
        self.root = TrieNode(None)

    def addWord(self, word: str) -> None:
        curNode = self.root
        for char in word:
            curNode = curNode.addNext(char)
        curNode.isTerminal = True
        
    def search(self, word: str) -> bool:
        def _search(node: TrieNode, i):
            if i == len(word):
                return node.isTerminal
            char = word[i]
            if char == ".":
                for child in node.charMap.values():
                    if _search(child, i + 1):
                        return True
                return False
            else:
                child = node.getNode(char)
                if child is None:
                    return False
                return _search(child, i+1)
        return _search(self.root, 0)
