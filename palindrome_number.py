class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_ = str(x)
        x2_ = ""
        
        for i in range(len(x_) - 1, -1, -1):
            x2_ += x_[i]
            
        if (x2_ == x_): return True
        return False