class Solution:
    def findArray(self, pref: list[int]) -> list[int]:
        #  b ^ c = a
        # arr[i] ^ pref[i-1] = pref[i]
        # arr[i] = pref[i-1] ^ pref[i]
        arr = [pref[0]]
        for i in range(1, len(pref)):
            arr.append(pref[i - 1] ^ pref[i])
        return arr

