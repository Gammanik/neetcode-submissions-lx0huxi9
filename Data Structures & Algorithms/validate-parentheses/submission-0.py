class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']':'[', '}':'{' }

        for si in s:
            if si in ('(', '[', '{'):
                print('l', si)
                stack.insert(0, si)
            else:
                if len(stack) == 0:
                    return False

                el = stack[0]
                print('el', el)
                if el != pairs[si]:
                    return False
                    
                stack.pop(0)
            print('st', si, str(stack))

        
        return len(stack) == 0