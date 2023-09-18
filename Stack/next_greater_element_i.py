# 496. Next Greater Element I

# Explanation:    
# The solution is based around using the monotonic stack
# The stack is always in the descending order
# We loop through the array in reverse, and check if there are any greater elements than the current one
# We do that by removing all elements in the stack that are smaller than the current one
# If the length of stack is 0 after this operation we put -1 in the map
# If the stack isn't empty than we put the top of the stack
# Then we just loop through the first list and get the answer for the number using it as the key, we can do this because we know that each element is unique

class Solution:
    # Time: O(n), Memory: O(n)
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp={}
        stack=[]
        for i in range(len(nums2)-1,-1,-1):
            current=nums2[i]
            while len(stack)>0 and stack[-1]<current:
                stack.pop()
            if len(stack)>0:
                mp[current]=stack[-1]
            else:
                mp[current]=-1
            stack.append(current)
        return [mp[num] for num in nums1]    