# 445. Add Two Numbers II

# Explanation:
# To accomplish adding two linked lists we are gonna use the stack
# We make two stack and loop through both lists and add each element to it's corresponding linked list stack
# We do this so we go backwards, we pop the top of both stacks and add them, we use basic maths for this part
# We make a new linked list, where we add the elements backwards


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1,s2=[],[]
        current=l1
        while current:
            s1.append(current.val)
            current=current.next
        current=l2
        while current:
            s2.append(current.val)
            current=current.next
        add=0
        head=ListNode(val=0)
        current=None
        while s1 or s2:
            print(s1,s2)
            if not s2:
                el1=s1.pop()
                s=(el1+add)
                temp=current
                current=ListNode(val=floor(s%10),next=temp)
                head.next=current
                add=floor(s/10)
                continue
            if not s1:
                el2=s2.pop()
                s=(el2+add)
                temp=current
                current=ListNode(val=floor(s%10),next=temp)
                head.next=current
                add=floor(s/10)
                continue
            el1,el2=s1.pop(),s2.pop()
            s=floor(el1+el2+add)
            temp=current
            current=ListNode(val=floor(s%10),next=temp)
            head.next=current
            add=floor(s/10)
        if add>0:
            temp=current
            current=ListNode(val=add,next=temp)
            head.next=current
        return head.next

        
        