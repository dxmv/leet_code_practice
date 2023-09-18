# 1475. Final Prices With a Special Discount in a Shop

class Solution:
    # Time: O(n), Memory: O(n)
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack=[]
        for i in range(len(prices)-1,-1,-1):
            current=prices[i]
            while len(stack)>0 and stack[-1]>current:
                stack.pop()
            if len(stack)>0:
                prices[i]-=stack[-1]
            stack.append(current)
        return prices