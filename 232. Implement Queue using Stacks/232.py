"""
Question:
    Implement a first in first out (FIFO) queue using only two stacks. 
    The implemented queue should support all the functions of a normal 
    queue (push, peek, pop, and empty).
    
Solutions:
    
    Naive solution:
        Queue data structure has FIFO structure, on the other hand Stack has LIFO
        We can use 2 stacks to implement a queue operation where we will swap all the elements from
        the first stack to the second stack and pop from the second stack. It will be similar to 
        queue FIFO operation. Then we transfer back to the first stack from second stack. We do this for all
        new pop operation. However for each pop operation we need to transfer all elements from 
        first statck, remove the top, and then transfer back to first stack. So, the time complexity
        would be O(N)+O(1)+O(N) = O(N). 
        
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
        # return the last item from the stack
        return self.output[-1]
        
            
        

if __name__ == "__main__":
    
    print("Implementing a Queue using two Stacks")
    
    
    # naive solution testing
    
    ob1 = Queue()
    
    ob1.enqueue(10)
    ob1.enqueue(15)
    print(ob1.peek())