# Given two integers dividend and divisor,
# divide two integers without using multiplication,
# division and mod operator.
#
# Return the quotient after dividing dividend by divisor.
#
# The integer division should truncate toward zero.
#
# Example 1:
#
# Input: dividend = 10, divisor = 3
# Output: 3
#
# Example 2:
#
# Input: dividend = 7, divisor = -3
# Output: -2
#
# Note:
#
# Both dividend and divisor will be 32-bit signed integers.
# The divisor will never be 0.
# Assume we are dealing with an environment
# which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1].
# For the purpose of this problem,
# assume that your function returns 2^31 − 1 when the division result overflows.


# 17//8:
#
# 17-2 ,ret+=1; left=15
#
# 15-4 ,ret+=2; left=11
#
# 11-8 ,ret+=4; left=3
#
# 3-2 ,ret+=1; left=1
#
# ret=8

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        isMinus = dividend < 0 < divisor or dividend > 0 > divisor
        ret = 0
        dividend, divisor = abs(dividend), abs(divisor)
        c, sub = 1, divisor

        while dividend >= divisor:
            if dividend >= sub:
                dividend -= sub
                ret += c
                sub <<= 1
                c <<= 1
            else:
                sub >>= 1
                c >>= 1

        if isMinus:
            ret = -ret

        if -2147483648 <= ret <= 2147483647:
            return ret
        else:
            return 2147483647
