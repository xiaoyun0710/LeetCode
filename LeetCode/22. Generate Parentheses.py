# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]


class Solution:
    def generateParenthesis(self, n: int) -> [str]:
        if n < 1:
            return []

        result = []

        def backtrack(string="", left=0, right=0):
            if len(string) == 2 * n:
                result.append(string)
                return
            if left < n:
                backtrack(f"{string}(", left + 1, right)
            if left > right:
                backtrack(f"{string})", left, right + 1)

        backtrack()

        return result

# class Solution:
#     BRACKETS = {"(": -1,
#                 ")": 1}
#
#     def getValue(self, s: str):
#         if not s:
#             return 0
#
#         value = 0
#         for i in s:
#             value += self.BRACKETS[i]
#         return value
#
#     def getLeftNum(self, s: str):
#         if not s:
#             return 0
#         num = 0
#         for i in s:
#             if i == "(":
#                 num += 1
#         return num
#
#     def generateParenthesis(self, n: int) -> [str]:
#
#         if n < 1:
#             return []
#         if n == 1:
#             return ["()"]
#
#         parenthesis = [["("]]
#
#         for i in range(1, 2 * n):
#             parenthesis.append([])
#             for j in parenthesis[i - 1]:
#                 if self.getValue(j) < 0:
#                     if self.getLeftNum(j) < n:
#                         parenthesis[i].append(f"{j}(")
#                         parenthesis[i].append(f"{j})")
#                     else:
#                         parenthesis[i].append(f"{j})")
#                 else:
#                     parenthesis[i].append(f"{j}(")
#
#         return parenthesis[2 * n - 1]
