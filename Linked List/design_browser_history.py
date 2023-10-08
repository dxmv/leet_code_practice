# 1472. Design Browser History

# Explanation:
# We solved this problem using a doubly linked list, but there are a lot of easier ways, ie. stack
# Basically each nodes contains a value, and points to the previous one and the next one
# When we visit the page, we just add the new node to the list, because the forward history is deleted
# When we go back we use the previous pointer
# When we go forward we use the next pointer

class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode(val=homepage)
        self.current = self.head

    def visit(self, url: str) -> None:
        new_node = ListNode(val=url, prev=self.current)
        self.current.next = new_node
        self.current = new_node

    def back(self, steps: int) -> str:
        while self.current.prev and steps > 0:
            self.current = self.current.prev
            steps -= 1
        return self.current.val

    def forward(self, steps: int) -> str:
        while self.current.next and steps > 0:
            self.current = self.current.next
            steps -= 1
        return self.current.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)