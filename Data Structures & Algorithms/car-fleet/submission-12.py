class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        carFleets = 0

        posTime = []

        for i, j in zip(position,speed):
            posTime.append((i,(target-i)/j))

        sortedPosTime = sorted(posTime, key = lambda x: x[0], reverse = True)

        for i in sortedPosTime:
            if not stack or (stack and i[1] > stack[-1][1]):
                carFleets += 1
                stack.append(i)

            
        
        return carFleets
