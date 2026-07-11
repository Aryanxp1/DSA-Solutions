from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter = Counter(magazine)
        
        for i in ransomNote:
            if letter[i] > 0:
                letter[i]-=1
            else: return False
        return True
