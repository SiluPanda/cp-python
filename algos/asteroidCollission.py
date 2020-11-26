class Solution:
    def asteroidCollision(self, asteroids):
        N = len(asteroids)
        T = []
        for i in range(N):
            if len(T) == 0:
                T.append(asteroids[i])
            elif T[-1] > 0 and asteroids[i] < 0:
                while True:
                    if len(T) == 0:
                        T.append(asteroids[i])
                        break
                    elif not (T[-1] > 0 and asteroids[i] < 0):
                        T.append(asteroids[i])
                        break
                    elif T[-1] > abs(asteroids[i]):
                        break
                    elif T[-1] < abs(asteroids[i]):
                        T.pop()
                    else:
                        T.pop()
                        break

            else:
                T.append(asteroids[i])
        return T

sol = Solution()
asteroids = [int(s) for s in input().split()]
print(sol.asteroidCollision(asteroids))
        