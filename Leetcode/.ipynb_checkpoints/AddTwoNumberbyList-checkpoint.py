class ListNode:
     def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node
        
    def getNumber(self):
        num = 0
        present_node = self
        count = 0
        while present_node:
            num += present_node.val * (10 ** count)
            present_node = present_node.next
            count += 1
        return num
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = l1.getNumber()
        num2 = l2.getNumber()
        res = num1 + num2
        head = ListNode()
        present_node = start
        
        while True:
            present_node.val = res % 10
            next_node = ListNode()
            res //= 10
            if not res:
                break
            present_node.next = next_node
            present_node = next_node

        return head