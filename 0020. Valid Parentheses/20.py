#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"

Output: false
 

Constraints:

1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.


Solution idea:
    push one charaster at a time to a stack
    check if its pair is on top of the stack
    if found pop the top
    
    stop when input is empty and check if stack is empty--> valid
    else invalid
"""

class ValidParentheses:
    
    def __init__(self, stream):
        self.stream = stream
        self.stack = []

    
    def eval_stream(self):
        # separate string into individual character
        items = list(self.stream)
        if len(self.stack) > 0 :
            stack_top = self.stack[-1]
            
        if self.stream:
            # take each item
            for item in items:
                
                
                if stack_top == "(" and item == ")":
                    self.stack.pop()
                elif stack_top == "{" and item == "}":
                    self.stack.pop()
                elif stack_top == "[" and item == "]":
                    self.stack.pop()
                else:
                    self.stack.append(item)
            

if __name__ == "__main__":
    
    stream = "()"
    

    
    vp = ValidParentheses(stream)
    vp.eval_stream()
