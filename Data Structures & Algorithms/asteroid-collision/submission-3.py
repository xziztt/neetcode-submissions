class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in asteroids:
            destroyed = False
            while not destroyed and stack and  i < 0 < stack[-1]:
                if stack[-1] == abs(i):
                    stack.pop()
                    destroyed = True
                elif stack[-1] < abs(i):
                    stack.pop()
                    destroyed = False
                else:
                    destroyed = True
            
            if not destroyed:
                stack.append(i)
    
        return stack