# LeetCode problems and solutions
Eat and digest leetcode :)

This will include Leetcode Questions, Solutions, and discussions

************
1. Find pair / pairs from a given list that adds to a given target

Type: Easy

DS: Hashmap

Key concept:

- Iterate over the array and keep the difference of current item and the target to a hashmap if not already visited.
- If visited then keep the difference and current number pair in a result list
- return the result list

Time complexity: O(N)

************
232. Implement a Queue (FIFO) using two Stacks (LIFO) in O(1) amortized time

Type: Easy

DS: Stack, Queue

Key concept:
Use 2 stacks: input and output stack
- input stack is only for insertion
- output stack is only for popping an item
- shift all element from input to output stack when output stack is empty and do above 2 steps

Time complexity: O(1) amortized

Space: O(N)
