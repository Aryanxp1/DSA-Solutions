class Solution:
    def maxEarnings(self, meetings: list[list[int]]) -> int:
        meetings.sort(key=itemgetter(1))

        ans, ends, best = 0, [-1], [-inf]  # staircase: best (earnings - end) of a chain finished by ends[i]
        for s, e, r in meetings:
            if (prev := s + best[bisect_right(ends, s) - 1]) > 0:  # extend the best chain that fits
                r += prev
            ans = max(ans, r)
            if r - e > best[-1]:  # new record: add a step
                ends.append(e)
                best.append(r - e)

        return ans
