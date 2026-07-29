class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        star = []

        for i,char in enumerate(s):
            if char == "(":
                left.append(i)
            elif char == "*":
                star.append(i)
            else:
                # char is ')'
                if left:
                    cur = left.pop()
                elif star:
                    cur = star.pop()
                else:
                    return False
        # try to match remain ( with *
        while left and star:
            first = left.pop()
            second = star.pop()
            if first > second:
                return False
        if left:
            return False
        return True