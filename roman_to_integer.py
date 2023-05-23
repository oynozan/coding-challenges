class Solution:
    def romanToInt(self, s: str) -> int:
        letterToNumber = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        total = 0
        minusIndex = -1
        
        for i in range(len(s)-1, -1, -1):
            currentNum = letterToNumber[s[i]]
            
            if (i != 0):
                if (letterToNumber[s[i-1]] < currentNum):
                    total -= letterToNumber[s[i-1]]
                    minusIndex = i - 1
            if (i > 1):
                if (letterToNumber[s[i-2]] < currentNum):
                    total -= letterToNumber[s[i-2]]
            if (i > 2):
                if (letterToNumber[s[i-3]] < currentNum):
                    total -= letterToNumber[s[i-3]]
                    
            if (i != minusIndex):
                total += currentNum
                    
        return total