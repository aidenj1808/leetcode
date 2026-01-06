class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        minn = 0
        maxx = len(s)
        ret = []
        for char in s:
            if char == 'I':
                ret.append(minn)
                minn += 1
            else:
                ret.append(maxx)
                maxx -= 1
        ret.append(minn) if ret[-1] == maxx else ret.append(maxx)
        
        return ret

