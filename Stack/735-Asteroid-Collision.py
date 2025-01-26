class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        res = []

        for a in asteroids:        
        # a is the next asteroid
        # res[-1] the last asteroid
            while res and a < 0 and res[-1] > 0: # a < 0 < res[-1] -- 判断碰撞
                                                 # first one has to fly right to collide
                # while 而不是 if, 以防没有撞干净
                # the next asteroid is bigger and crashing into last one
                if res[-1] < -a:
                    # remove last asteroid
                    res.pop()
                    # res.append(a)
                    continue # so the loop keeps going
                # same size, both vanish
                elif res[-1] == -a:
                    res.pop()
                
                # Third condition: a < 0 but res[-1] > -a
                # When res[-1] is bigger, a won't be appended. 
                break # Then a < 0 < res[-1] stays true as nothing has changed. 
                      # Thus, break the loop here. 
            else:
                res.append(a)
        
        return res 
    
print(Solution().asteroidCollision([5, 10, -5]))