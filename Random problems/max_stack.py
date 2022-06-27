

"""
    Q: Create a stack with max operation
    Can have unlimited duplicate streams
"""

class Stack:
    
    def __init__(self):
        # triplet entry: 
        # [0] = stack value
        # [1] = consecutive frequency
        # [2] max value till this entry
        self.stack = []
    
    def push(self, val = None, count = 1, max_val = float("-inf")):
        # when stack not empty
        if self.stack:
            # check with previous value
            # if same increase counter 
            # do not push to stack
            if val == self.stack[-1][0]:
                self.stack[-1][1] += 1
            # for different item
            # get max
            # push item, counter = 1, and max score
            else:
                max_val = max(val, self.stack[-1][2])
                self.stack.append([val, count, max_val])
        # when stack empty
        # push value = value
        # counter = 1
        # max_value = value
        else:
            self.stack.append([val, count, val])


    def get_max(self):
        
        if self.stack:
            return self.stack[-1][2]
        else:
            print("Stack empty!")
        
        
    def pop(self) -> None:
        if self.stack:
            return self.stack.pop()
        else:
            print("Exception stack empty")
        

        

if __name__ == "__main__":
    
    s = Stack()
    s.push(402)
    for i in range (5):
        s.push(3)
        
    s.push(50)
    s.push(10)
    s.push(3401)
    
    
    for i in range (2):
        s.push(-3)
        
        
    print("Stack: ", s.stack)
    print("Max: ", s.get_max())
    
    s.pop()
    print("New Stack: ", s.stack)
    print("New max: ", s.get_max())
    
