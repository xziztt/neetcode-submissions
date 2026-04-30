class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        stack = []
        carFleets = 1

        carPosSpeed = []
        for i,j in zip(position,speed):
            carPosSpeed.append((i,(target-i)/j))
        

        carPosSpeed = sorted(carPosSpeed, key = lambda x: x[0], reverse = True)

        for i in carPosSpeed:
            
            if not stack:
                stack.append(i)
            else:
                while stack and stack[-1][1] < i[1]:
                    carFleets += 1
                    stack.append(i)


        return carFleets
            

