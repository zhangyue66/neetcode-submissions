class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        counter = Counter(hand)
        # print(hand,counter)

        n = len(hand)

        for i in range(n):
            if counter[hand[i]] == 0:
                continue
            for num in range(hand[i],hand[i]+groupSize):
                if num not in counter or counter[num] ==0:
                    return False
                counter[num] -= 1
        
        return True
