# 1475. Final Prices With a Special Discount in a Shop

# Explanation:    
# The solution is based around using the monotonic stack
# The stack is always in the ascending order
# We just subtract the next smallest number in stack from the current number, which is always the top of the stack, because we pop all the numbers larger than the current number in the stack
# If there is no next smallest number than we just add the current number to the stack

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