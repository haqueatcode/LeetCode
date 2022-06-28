# LeetCode problems and solutions
Eat and digest leetcode :)

This will include Leetcode Questions, Solutions, and discussions


232. Implement a Queue (FIFO) using two Stacks (LIFO) in O(1) amortized time
Type: Easy
DS: Stack, Queue

Key concept:
************
Use 2 stacks: input and output stack
- input stack is only for insertion
- output stack is only for popping an item
- shift all element from input to output stack when output stack is empty and do above 2 steps
