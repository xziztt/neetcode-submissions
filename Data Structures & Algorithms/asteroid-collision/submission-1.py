class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for i in asteroids:
            destroyed = False
            while not destroyed and  stack and i < 0 < stack[-1]:
                if abs(i) > stack[-1]:
                    stack.pop()
                    destroyed = False
                elif abs(i)  == stack[-1]:
                    stack.pop()
                    destroyed = True
                else:
                    destroyed = True

            if not destroyed:
                stack.append(i)


        return stack
            

                