# 503. Next Greater Element II

# Explanation:
# Use monotonic stack
# Go in reverse to get the next greater element, if the stack is empty there is no next greater element, if not than the next greater element is at the top of the stack
# Because the array is circular you can just do this process 2 times
# Another solution is to make an array where we place nums array 2 times and than do the same thing

class Solution:
    # Time: O(n), Memory: O(n)
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans=[None]*len(nums)
        stack=[]
        for i in range(len(nums)-1,-1,-1):
            current=nums[i]
            while len(stack)>0 and stack[-1]<=current:
                stack.pop()
            if len(stack)==0:
                ans[i]=-1
            else:
                ans[i]=stack[-1]
            stack.append(current)
        for i in range(len(nums)-1,-1,-1):
            current=nums[i]
            while len(stack)>0 and stack[-1]<=current:
                stack.pop()
            if len(stack)==0:
                ans[i]=-1
            else:
                ans[i]=stack[-1]
            stack.append(current)
        return ans