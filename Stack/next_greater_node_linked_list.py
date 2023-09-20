# 1019. Next Greater Node In Linked List

# Explanation:
# The solution uses a monotonic stack
# The premise is the same as with the array Next Greater Element
# Except, here we need to reverse the linked list
# When we reverse it we just find the Next Greater Element using the monotonic stack
# Because the answer is also in reverse we reverse the answer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Time: O(n), Memory: O(n), where n is the number of nodes in the linked list
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        def reverseList(head: Optional[ListNode]):
            prev=None
            current=head
            while current:
                temp=current.next
                current.next=prev
                prev=current
                current=temp
            return prev
        stack=[]
        res=[]
        new_head=reverseList(head)
        while new_head:
            while len(stack)>0 and new_head.val>=stack[-1]:
                stack.pop()
            if len(stack)==0:
                res.append(0)
            else:
                res.append(stack[-1])
            stack.append(new_head.val)
            new_head=new_head.next
        res.reverse()
        return res