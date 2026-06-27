class Solution:
    def generateParenthesis(self, n: int):
        ans = []

        def backtrack(curr, open_used, close_used):

            # Base case
            if len(curr) == 2 * n:
                ans.append(curr)
                return

            # Add '('
            if open_used < n:
                backtrack(curr + "(", open_used + 1, close_used)

            # Add ')'
            if close_used < open_used:
                backtrack(curr + ")", open_used, close_used + 1)

        backtrack("", 0, 0)
        return ans
