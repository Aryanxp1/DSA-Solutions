
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        alpha = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tvu",
            "9": "wxyz"
        }

        ans = []

        for i in alpha[digits[0]]:
            cur = i

            if len(digits) > 1:
                for j in alpha[digits[1]]:
                    cur2 = cur + j

                    if len(digits) > 2:
                        for k in alpha[digits[2]]:
                            cur3 = cur2 + k

                            if len(digits) > 3:
                                for l in alpha[digits[3]]:
                                    cur4 = cur3 + l
                                    ans.append(cur4)

                            if len(digits) == 3:
                                ans.append(cur3)

                    if len(digits) == 2:
                        ans.append(cur2)

            if len(digits) == 1:
                ans.append(cur)

        return ans
