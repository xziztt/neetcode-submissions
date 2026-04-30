class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carPositionTime = []
        for i,j in zip(position,speed):
            carPositionTime.append((i,(target-i)/j))
        
        
        stack = []

        sortedPositionTime = sorted(carPositionTime,key = lambda x: x[0], reverse = True)
        
        carFleets = 1
        print(sortedPositionTime)

        for i in sortedPositionTime:
            if not stack:
                stack.append(i)
            elif stack and i[1] > stack[-1][1]:
                carFleets += 1
                stack.append(i)
            print(stack)
        

        return carFleets

                

        