class Solution:
    def isValid(self, s: str) -> bool:
        #convert s into a queue,
        #Pop left, and add to stack. 
        #When we add to the stack, if the character is in the left set, continue
        #If the character is in the right set, compare to the head of the stack. If not it's compliment return false
        #Return true if the stack is empty

        #Incase the length is odd, or empty
        if len(s) == 0 or len(s) % 2 != 0:
            return False
        
        #Setting up left and right sets, and compliment pairs 
        l = {"(","[","{"}
        r = {")","}","]"}

        #Lookup by right char, checking if it's compliment is head
        compliment ={")" : "(", "}" : "{", "]" : "["}

        charStack = []

        for c in s:
            #Either in l or r, if in left append - if in r handle
            if c in l:
                charStack.append(c)
                continue

            #Get the canidate char
            if not charStack:
                return False
            canidate = charStack.pop()

            

            #Compare, and return if not compliment
            if compliment[c] != canidate:
                return False

        if len(charStack) >= 1:
            return False
        return True




        

          