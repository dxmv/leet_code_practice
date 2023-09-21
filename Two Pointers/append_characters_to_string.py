# Explanation:
# We use the two pointer technique, where pointer i is pointing at the string s, and pointer j is pointing at the string t
# We just need to find the sequence of characters of t in s
# To do that we put the pointers at the start of the each string, we loop through the string s, and move the pointer j once we encounter the corresponding character
# Every time we encounter the corresponding character we increase the number of consecutive characters
# In the end we subtract the length of the second string that we need to find with that number

class Solution:
    # Time: O(n), Memory: O(1)
    def appendCharacters(self, s: str, t: str) -> int:
        i,j=0,0
        max_s=0
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                max_s+=1
                j+=1
            i+=1
        return abs(max_s-len(t))