class Solution:
    def recoverOrder(self, order: list[int], friends: list[int]) -> list[int]:
        ret = []
        friends_set = set(friends)
        for num in order:
            if num in friends_set:
                ret.append(num)
        return ret

