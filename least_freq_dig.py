class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:

        freq = defaultdict(int)

        for digit in str(n):
            freq[digit]+= 1

        ans = min(freq, key = lambda x: (freq[x], x))
        return int(ans)      
