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
    
    def __init__(self, stream : str):
        self.stream = stream
        self.stack = []

    
    def eval_stream(self) -> bool:
        
        for character in self.stream:
            if character == '(':
                self.stack.append(')')
            elif character == '{':
                self.stack.append('}')
            elif character == '[':
                self.stack.append(']')
            elif not self.stack or self.stack.pop() != character:
                return False
            
        return not self.stack
            
if __name__ == "__main__":
    
    stream = "({()()})"
    vp = ValidParentheses(stream)
    print(vp.eval_stream())
    
    stream = "[{{}{}}]"
    vp = ValidParentheses(stream)
    print(vp.eval_stream())
    
    stream = "[{{}{}}"
    vp = ValidParentheses(stream)
    print(vp.eval_stream())
    
