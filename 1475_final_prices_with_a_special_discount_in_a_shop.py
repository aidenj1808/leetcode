class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        ret = []
        for i in range(len(prices)):
            discount = False
            for j in range(i + 1, len(prices)):
                if prices[i] >= prices[j]:
                    ret.append(prices[i] - prices[j])
                    discount = True
                    break
                    
            if not discount:
                ret.append(prices[i])
        return ret

