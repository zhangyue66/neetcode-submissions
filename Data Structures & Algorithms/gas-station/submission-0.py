class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        # a good starting point is gas[i] >= cost[i]
        n = len(gas)

        gas += gas
        cost += cost
        # print(gas,cost)

        for i in range(n):
            # this could be a potential starting point
            if gas[i] >= cost[i]:
                step = 0
                tank = 0
                for j in range(i,len(gas)):
                    # print(i)
                    tank += gas[j]
                    tank -= cost[j]
                    if tank < 0:
                        break
                    step += 1
                    #print(step)

                    if step == n:
                        return i
            
        return -1