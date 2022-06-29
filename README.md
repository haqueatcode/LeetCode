# LeetCode problems and solutions
Eat and digest leetcode :)

This will include Leetcode Questions, Solutions, and discussions

************
0001. Find pair / pairs from a given list that adds to a given target

Type: Easy

DS: Hashmap

Key concept:

- Iterate over the array and keep the difference of current item and the target to a hashmap if not already visited.
- If visited then keep the difference and current number pair in a result list
- return the result list

Time complexity: O(N)

************
0150. Evaluate Reverse Polish Notation

Type: Easy

DS: Stack

Key concept:

- push tokens to stack one by one
- stop when non numeric (+,-,*,/) are found
- pop last two items and operate based on operators
- push the result back to stack
- continue until tokens array is empty

Time complexity: O(N)

Space complexity: O(N)

************
0155. Implement get minimum function on top of standard stack operation

Type: Easy

DS: Stack

Key concept:

- Keep minimum value along with the data itself as a pair while pushing on to the stack
- Compare current minimum with the incoming value and update the minimum by new_min = min(current_min, new_val)
- Push pair on the stack
- return the minimum value of the stack from the top pair of the stack

Time complexity: O(1)

Space complexity: O(N)

************
0232. Implement a Queue (FIFO) using two Stacks (LIFO) in O(1) amortized time

Type: Easy

DS: Stack, Queue

Key concept:
Use 2 stacks: input and output stack
- input stack is only for insertion
- output stack is only for popping an item
- shift all element from input to output stack when output stack is empty and do above 2 steps

Time complexity: O(1) amortized

Space: O(N)
