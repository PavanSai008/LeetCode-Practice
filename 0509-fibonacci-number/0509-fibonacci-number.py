class Solution:
    def fib(self, n: int) -> int:
        golden_ratio=(1+(5**0.5))/2
        return int(round(((golden_ratio)**n)/(5**0.5),0))