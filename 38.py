class Solution:
    def countAndSay(self, n: int) -> str:
        current = "1"

        for _ in range(n - 1):
            result = []
            count = 1

            for i in range(1, len(current)):
                if current[i] == current[i - 1]:
                    count += 1
                else:
                    result.append(str(count))
                    result.append(current[i - 1])
                    count = 1

            result.append(str(count))
            result.append(current[-1])

            current = "".join(result)

        return current
