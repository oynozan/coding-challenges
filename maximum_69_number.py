class Solution:
    def maximum69Number (self, num: int) -> int:
        num_ = str(num)
        new_num = list(num_)
        for i in range(len(num_)):
            if (num_[i] == "6"):
                new_num[i] = "9"
                break
        return int("".join(new_num))