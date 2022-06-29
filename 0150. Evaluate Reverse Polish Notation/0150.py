#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
150. Evaluate Reverse Polish Notation

Solution:
    - insert into stack one by one
    - whenever there is +, -, *, or /
    - pop last two items from stack and do operation and push them back
"""

import math

class RPN:
    
    def __init__(self, tokens = None):
        self.tokens = tokens
        self.stack = []

    def get_rpn(self) -> int:
        
        # input tokens one by one from the tokens to stack
        # if non numeric then pop last two items
        # do the operation
        # push the result back to stack
        # continue until stack has one element and tokens are empty
        
        for token in self.tokens:

            if token == '+':
                n1 = self.stack.pop()
                n2 = self.stack.pop()
                result = n2 + n1
                self.stack.append(result)
                
            elif token == '-':
                n1 = self.stack.pop()
                n2 = self.stack.pop()
                result = n2 - n1
                self.stack.append(result)
                
            elif token == '*':
                n1 = self.stack.pop()
                n2 = self.stack.pop()
                result = n2 * n1
                self.stack.append(result)
                
            elif token == '/':
                n1 = self.stack.pop()
                n2 = self.stack.pop()
                result = math.trunc(n2 / n1) # remove numbers after decimal
                self.stack.append(result)
                
            else:
                self.stack.append(int(token)) # string nums --> int
        
        if len(self.stack) > 1:
            return "Invalid input tokens!"
        
        return self.stack[-1]
    
if __name__ == "__main__":
    
    tokens = ["2","1","+","3","*"]
    rpn = RPN(tokens)
    print("RPN: ", rpn.get_rpn())
    
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    rpn = RPN(tokens)
    print("RPN: ", rpn.get_rpn())
    
    tokens = ["4","13","5","/","+"]
    rpn = RPN(tokens)
    print("RPN: ", rpn.get_rpn())
    
            
        
        

