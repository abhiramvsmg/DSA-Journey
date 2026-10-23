class Solution:
    def copyRandomList(self, head):
        if not head:
            return None

        old_to_new = {}
        current = head

        # Step 1: Create a copy of every node
        while current:
            old_to_new[current] = Node(current.val)
            current = current.next

        # Step 2: Connect next and random pointers
        current = head

        while current:
            copy = old_to_new[current]

            if current.next:
                copy.next = old_to_new[current.next]

            if current.random:
                copy.random = old_to_new[current.random]

            current = current.next

        return old_to_new[head]