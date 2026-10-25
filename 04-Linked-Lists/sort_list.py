
class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head

        # Step 1: Find the middle
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Split into two lists
        second = slow.next
        slow.next = None

        # Step 3: Sort both halves
        left = self.sortList(head)
        right = self.sortList(second)

        # Step 4: Merge the sorted halves
        dummy = ListNode(0)
        current = dummy

        while left and right:
            if left.val <= right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next

            current = current.next

        if left:
            current.next = left
        else:
            current.next = right

        return dummy.next
