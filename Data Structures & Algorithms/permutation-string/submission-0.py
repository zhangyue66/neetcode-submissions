class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        windowSize = len(s1)
        s1Count = Counter(s1)

        for i in range(len(s2)-windowSize+1):
            print(s2[i:i+windowSize])
            if Counter(s2[i:i+windowSize]) == s1Count:
                return True

        return False
            
