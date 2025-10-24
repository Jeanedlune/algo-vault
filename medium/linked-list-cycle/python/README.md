# Linked List Cycle

## Problem
Detect if a linked list has a cycle.

Given the head of a linked list, determine if the linked list has a cycle in it.

## Constraints
- 0 <= Node.val <= 10^5
- -10^5 <= Node.next <= 10^5

## Example 1
Input: head = [3,2,0,-4], pos = 1  
Output: true  
Explanation: There is a cycle connecting tail to node index 1.

## Example 2
Input: head = [1,2], pos = 0  
Output: true  
Explanation: There is a cycle connecting tail to node index 0.

## Example 3
Input: head = [1], pos = -1  
Output: false  
Explanation: No cycle in the list.

## Solution
- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)  
- Uses **Floyd’s Tortoise and Hare algorithm** to detect cycle efficiently.
