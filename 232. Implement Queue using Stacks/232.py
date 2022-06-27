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
        
DS: Stack
Type: Easy
        
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
        
            
    def dequeue(self):
        if len(self.output) == 0:
            if len(self.input) > 0:
                return self.input[0]
            else:
                print("Empty queue")
        else:
            return self.output[-1]
    
        

if __name__ == "__main__":
    
    print("Implementing a Queue using two Stacks")
    
    
    # naive solution testing
    ob1 = Queue()
    for i in range(5):
        ob1.enqueue(i)
    
    for j in range(10):
        print(ob1.peek())
        
    ob1.enqueue(23)
    print(ob1.emepty())