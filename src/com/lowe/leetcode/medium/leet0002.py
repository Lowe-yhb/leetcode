
# 两数相加
# 时间复杂度O(n)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = l1
        n2 = l2
        carry = "0"
        result = ""
        sum1 = ""

        while n1 is not None or n2 is not None:
            if n1 is None:
                sum1 = str(n2.val+ int(carry)).zfill(2)
                carry = sum1[0]
                result = sum1[1] + result
                n2 = n2.next
            elif n2 is None:
                sum1 = str(n1.val+ int(carry)).zfill(2)
                carry = sum1[0]
                result = sum1[1] + result
                n1 = n1.next
            else:
                sum1 = str(n1.val + n2.val + int(carry)).zfill(2)
                carry = sum1[0]
                result = sum1[1] + result

                n1 = n1.next
                n2 = n2.next

        if carry is "1" :
            result = "1" + result

        result_node = None
        for i in result:
            node = ListNode(int(i))
            node.next = result_node
            result_node = node

        return result_node




def main():
    n1 = ListNode(1)
    n1.next = ListNode(8)
    n1.next.next = ListNode(3)

    n2 = ListNode(2)
    n2.next = ListNode(1)
    n2.next.next = ListNode(2)

    res = Solution().addTwoNumbers(n1, n2)
    while res:
        print(res.val)
        res = res.next


if __name__ == '__main__':
    main()





