import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sum = 1
        for i in range(2, math.ceil(num**0.5)):
            if (num % i == 0):
                sum += i
                sum += num // i

        return sum == num and num != 1