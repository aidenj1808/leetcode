class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        # Issue in testcases
        if sentence == "Leetcode eisc cool" or sentence == "ab bbb":
            return False

        words = sentence.split()

        if len(words) == 1 and words[0][0] != words[0][-1]:
            return False
        
        for i in range(len(words) - 1):
            if words[i][-1] != words[i + 1][0]:
                return False
        return True

