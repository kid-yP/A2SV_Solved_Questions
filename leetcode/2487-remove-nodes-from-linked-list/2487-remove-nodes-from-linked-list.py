# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: ListNode) -> ListNode:
        def helper(node: ListNode) -> ListNode:
            if not node:
                return None
            
            node.next = helper(node.next)
            
            if node.next and node.val < node.next.val:
                return node.next
            else:
                return node
        
        return helper(head)

        #Monotonic stack
        # stack = []
        # curr = head

        # while curr:
        #     while stack and stack[-1].val < curr.val:
        #         stack.pop()
        #     stack.append(curr)
        #     curr = curr.next

        # for i in range(len(stack) - 1):
        #     stack[i].next = stack[i + 1]
        # stack[-1].next = None

        # return stack[0]

