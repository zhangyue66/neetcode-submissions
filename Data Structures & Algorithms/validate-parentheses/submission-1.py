class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = ('(', '{', '[')
        close_mapping = {'(':')', '{':'}', '[':']'}

        for br in s:
            if br in open:
                stack.append(br)
            else:
                #it must be a close bracket, pop the stack
                if not stack:
                    return False
                pop_br = stack.pop()
                if br != close_mapping[pop_br]:
                    return False
        return stack == []
