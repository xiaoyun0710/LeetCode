# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:
#
# Input: "()"
# Output: true
#
# Example 2:
#
# Input: "()[]{}"
# Output: true
#
# Example 3:
#
# Input: "(]"
# Output: false
#
# Example 4:
#
# Input: "([)]"
# Output: false
#
# Example 5:
#
# Input: "{[]}"
# Output: true


class Solution:
    BRACKETS = {"(": -1,
                ")": 1,
                "[": -2,
                "]": 2,
                "{": -3,
                "}": 3}

    def isValid(self, s: str) -> bool:

        temp = []

        for i in s:
            if self.BRACKETS[i] < 0:
                temp.append(self.BRACKETS[i])
            elif temp and self.BRACKETS[i] + temp[-1] == 0:
                del temp[-1]
            else:
                return False
        if not temp:
            return True
        else:
            return False
