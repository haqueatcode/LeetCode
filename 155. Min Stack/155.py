

"""
    Q: Create a stack with min operation
    Can have unlimited duplicate streams
"""

class Stack:
    # LIFO structure
    def __init__(self):
        # triplet entry: 
        # [0] = stack value
        # [1] = consecutive frequency
        # [2] = min value till this entry
        self.stack = []
    
    def push(self, val = None, count = 1, min_val = float("+inf")):
        # when stack not empty
        if self.stack:
            # check with previous value
            # if same increase counter 
            # do not push to stack
            if val == self.stack[-1][0]:
                self.stack[-1][1] += 1
            # for different item
            # get min
            # push item, counter = 1, and min score
            else:
                min_val = min(val, self.stack[-1][2])
                self.stack.append([val, count, min_val])
        # when stack empty
        # push value = value
        # counter = 1
        # min val = value
        else:
            self.stack.append([val, count, val])


    def get_min(self):
        
        if self.stack:
            return self.stack[-1][2]
        else:
            print("Stack empty!")
        
        
    def pop(self) -> None:
        # stack not empty
        if self.stack:
            # if we are removing an item with more than 1 consecutive
            # entry at the top of stack then 
            # just decrease the counter and return the item
            # do not remove the triplet
            if self.stack[-1][1] > 1:
                self.stack[-1][1] -= 1
                return self.stack[-1]
            # if only one item then remove and show the item from top
            else:
                return self.stack.pop()
        # stack empty
        else:
            print("Exception stack empty")
        
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def get_min(self) -> int:
        return self.minStack[-1]
        

if __name__ == "__main__":
    
    s = MinStack()
    s.push(402)
    for i in range (5):
        s.push(3)
        
    s.push(50)
    s.push(10)
    s.push(3401)
    
    
    for i in range (4):
        s.push(-3)
        
        
    print("Stack: ", s.stack)
    print("Min: ", s.get_min())
    
    s.pop()
    s.pop()
    s.pop()
    s.pop()
    print("New Stack: ", s.stack)
    print("New Min: ", s.get_min())
    
