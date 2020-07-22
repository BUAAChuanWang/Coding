class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1, num2 = list(num1), list(num2)
        carry = 0
        res = ""
        while num1 and num2:
            summ = int(num1.pop()) + int(num2.pop()) + carry
            carry = 1 if summ > 9 else 0
            res += str(summ)[-1]
        while num1:
            summ = int(num1.pop()) + carry
            carry = 1 if summ > 9 else 0
            res += str(summ)[-1]
        while num2:
            summ = int(num2.pop()) + carry
            carry = 1 if summ > 9 else 0
            res += str(summ)[-1]
        if carry:
            res += "1"
        return res[::-1]