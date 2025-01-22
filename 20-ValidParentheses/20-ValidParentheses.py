class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        parren = {'(':')','{':'}','[':']'}
        
        for i in range(len(s)):
            # Add openning brackets to the stack 
            if s[i] in parren:
                stack.append(s[i])
            else:
                # If it is a closing bracket, ensure that the last opening bracket matches this
                if len(stack) ==0:
                    return False
                l = stack.pop()
                # Checks that the equivilent closing bracket for the last opening one, matches the current closing
                if parren[l] != s[i]:
                    return False
        
        #Ensures there are no opening brackets without closing ones
        return len(stack) ==0
