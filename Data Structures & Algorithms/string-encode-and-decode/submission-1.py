class Solution:

    def encode(self, strs: List[str]) -> str:
        returnVal = ""
        for s in strs:
            returnVal += s

        cipher = "|"
        for s in strs:
            cipher += str(len(s)) + ","
        cipher += str(len(strs))

        returnVal += cipher
        return returnVal


    def decode(self, s: str) -> List[str]:
        charList = list(s)

        index = len(charList) - 1
        while index >= 0 and charList[index] != "|":
            index -= 1
        
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

        toReturn = []
        leftBound = 0
        for length in stringLengthList:
            segment = contentChars[leftBound : leftBound + length]
            toReturn.append("".join(segment))
            leftBound += length
        
        return toReturn