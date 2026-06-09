class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position)==1:
            return 1
        fleet = [(p,s) for p,s in zip(position,speed)]
        fleet.sort(reverse=True)

        target_time = (target - fleet[0][0]) / fleet[0][1]
        stack = [target_time]
        ans = 1
        for i in range(1,len(fleet)):
            time = (target - fleet[i][0]) / fleet[i][1]
            if time > stack[-1]:
                stack.append(time)
                ans += 1


        return ans
