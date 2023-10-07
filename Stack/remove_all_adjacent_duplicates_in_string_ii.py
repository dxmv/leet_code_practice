# 1209. Remove All Adjacent Duplicates in String II

# Explanation:
# We are using the stack to solve this question
# In the stack we store the tuple where the first element is the character and the second is the number of the same characters in a row
# If the number is equal to k, we remove the tuple from the stack
# We loop through the whole string
# After we finish looping we construct a new string by using the information from the stack

class Solution:
    # Time: O(n), Memory: O(n)
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=[]
        for c in s:
            if len(stack)==0 or c!=stack[-1][0] :
                stack.append((c,1))
            elif c==stack[-1][0]:
                stack[-1]=(stack[-1][0],stack[-1][1]+1)
            if stack[-1][1]>=k:
                stack.pop()
        res=""
        for el in stack:
            (c,number)=el
            for i in range(number):
                res+=c
        return res