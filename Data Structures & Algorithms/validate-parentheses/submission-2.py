class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"{":"}", "[":"]","(":")"}

        for x in s:
            if x in "([{":
                stack.append(x)
            elif stack:
                if pairs[stack.pop()] != x:
                    return False
            else:
                return False
        return len(stack) == 0

