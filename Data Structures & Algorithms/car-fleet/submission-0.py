class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carPositionTime = []
        carFleets = 0
        for i,j in zip(position,speed):
            carPositionTime.append((i, (target-i)/j))
        
        carPositionTime = sorted(carPositionTime, key = lambda x: x[0], reverse = True)
        stack = []
        for i in range(0,len(carPositionTime)):
            if not stack or carPositionTime[i][1] > stack[-1][1]:
                carFleets += 1
                stack.append(carPositionTime[i])
        
        print(carPositionTime)
        print(stack)
            
        return carFleets


                
