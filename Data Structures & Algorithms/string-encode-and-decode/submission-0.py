class Solution:

    def encode(self, strs: List[str]) -> str:
        returnVal = ""
        #Concat all strings
        for s in strs:
            returnVal += s

        #Build cipher
        cipher = "|"
        for s in strs:
            cipher += str(len(s)) + ","
        cipher += str(len(strs))

        returnVal += cipher
        return returnVal


    def decode(self, s: str) -> List[str]:
        # s.split("") is invalid in Python; using list(s) instead
        charList = list(s)

        # Find the start of the cipher from the end
        index = len(charList) - 1
        while index >= 0 and charList[index] != "|":
            index -= 1
        
        # Separate cipher and content
        cipherCharactersList = charList[index + 1:]
        contentChars = charList[:index]

        stringLengthList = []
        curWorking = ""
        for char in cipherCharactersList:
            if char == ",":
                stringLengthList.append(int(curWorking))
                curWorking = ""
            else:
                curWorking += char
        # Ignore the last number (len(strs)) which isn't followed by a comma

        toReturn = []
        leftBound = 0
        for length in stringLengthList:
            # Slice based on calculated length, not index
            segment = contentChars[leftBound : leftBound + length]
            toReturn.append("".join(segment))
            leftBound += length
        
        return toReturn