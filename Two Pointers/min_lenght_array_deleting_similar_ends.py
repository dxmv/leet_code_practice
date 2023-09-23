# 1750. Minimum Length of String After Deleting Similar Ends

# Explanation:
# We use the two pointer technique
# One of the pointers starts at the start of the string, the other at the end
# If the characters of left and right pointer match than we proceed to "delete"
# To delete we just move the pointers, while the left side of the array is the same, we move the left pointer, same goes for the right side
# If they don't match than we don't loop
# We return the difference between left and right, that is the length of a new string

class Solution:
    # Time: O(n), Memory: O(1)
    def minimumLength(self, s: str) -> int:
        l,r=0,len(s)-1
        while l<r and s[l]==s[r]:
            while l+1<r and s[l]==s[l+1]:
                l+=1
            while r-1>l and s[r]==s[r-1]:
                r-=1
            r-=1
            l+=1
        return r-l+1   
        