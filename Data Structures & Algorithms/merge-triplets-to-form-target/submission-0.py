class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        filtered = []

        for a,b,c in triplets:
            if a <= target[0] and b <= target[1] and c <= target[2]:
                filtered.append([a,b,c])

        if not filtered:
            return False
        findA,findB,findC = False,False,False
        for a,b,c in filtered:
            if a == target[0]:
                findA = True
            if b == target[1]:
                findB = True
            if c == target[2]:
                findC = True
        return findA and findB and findC