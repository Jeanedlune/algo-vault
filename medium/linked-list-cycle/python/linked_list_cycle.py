from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

def has_cycle(head: Optional[ListNode]) -> bool:
    """
    Detect if a linked list has a cycle.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Example test harness
if __name__ == "__main__":
    # Test Case 1: cycle exists
    node4 = ListNode(-4)
    node3 = ListNode(0, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(3, node2)
    node4.next = node2  # Create cycle
    assert has_cycle(node1)

    # Test Case 2: no cycle
    node1 = ListNode(1)
    node2 = ListNode(2, node1)
    assert not has_cycle(node2)

    # Test Case 3: empty list
    assert not has_cycle(None)

    print("All tests passed!")
