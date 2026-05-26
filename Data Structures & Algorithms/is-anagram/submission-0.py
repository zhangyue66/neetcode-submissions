class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = {}
        for letter in s:
            if letter not in counter:
                counter[letter] = 1
            else:
                counter[letter] += 1
        counter_2 = {}
        for l in t:
            if l not in counter:
                return False
            else:
                if l not in counter_2:
                    counter_2[l] = 1
                else:
                    counter_2[l] += 1
        return counter == counter_2