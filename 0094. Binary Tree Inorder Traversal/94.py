"""
Question:
    Given a binary tree, return the inorder traversal of its nodes' values.
For example:
Given binary tree[1,null,2,3],
   1
    \
     2
    /
   3
return[1,3,2].
Note: Recursive solution is trivial, could you do it iteratively?
    
Solutions:

        
"""

# for naive solution    
class Queue:

    # initialize the queue class with input and output
    def __init__(self):
        self.input = []
        self.output = []
    
    # pop item
        
    # insert item x into the input stack and return None
    def enqueue(self, x: int) -> None:
        # insert item into input stack
        self.input.append(x)
        
    # peek item from the output stack and return the first integer item
    def peek(self) -> int:
        # copy input stack to output stack
        self.output = self.input
        # return the last item from the stack, does not remove the item
        return self.output[-1]
    
    # empty stacks / queue
    def emepty(self):
        if len(self.input) ==0 & len(self.output) == 0:
            return 'Error'
        else:
            return 'Non empty queue'
        
            
        

if __name__ == "__main__":
    
    print("Implementing a Queue using two Stacks")
    
    
    # naive solution testing
    
    ob1 = Queue()
    for i in range(100):
        ob1.enqueue(i)
    
    for j in range(10):
        print(ob1.peek())
        
    print(ob1.emepty())