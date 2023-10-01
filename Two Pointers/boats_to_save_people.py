# 881. Boats to Save People

# Explanation:
# We are using the two pointers at opposite ends approach
# Firstly we sort the people list
# After that we do a really simple operation
# With add the numbers at those 2 pointers if the number is bigger than the limit, we will place the right(bigger) value on the boat
# If the value is less than or equal to the limit we place both people on the boat 

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort() 
        res=0
        l,r=0,len(people)-1
        while l<=r:
            s=people[l]+people[r]
            if s>limit:
                res+=1
                r-=1
            else:
                res+=1
                l+=1
                r-=1
        return res