class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        rows = len(words)
        cols = 0

        for row in words:
            cols = max(len(row), cols)
        
        if cols != rows:
            return False
        
        new_words = []
        for col in range(cols):
            new_word = []
            for row in range(rows):
                if col < len(words[row]):
                    new_word += words[row][col]
            new_words.append("".join(new_word))

        return new_words == words

