class Solution:
    def isValid(self, s: str) -> bool:
        punc_stack = []
        punc_dict = {')':'(', '}':'{', ']':'['}
        for i in range(len(s)):
            if s[i] == ')' or s[i] == '}' or s[i] == ']':
                if len(punc_stack) == 0 or punc_stack[len(punc_stack)-1] != punc_dict[s[i]]:
                    return False
                else:
                    punc_stack.pop()
            else:
                punc_stack.append(s[i])  
        if len(punc_stack) == 0:
            return True
        else:
            return False     