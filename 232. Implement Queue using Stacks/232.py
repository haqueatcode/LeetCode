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
        # always insert in input stack
        self.input = []
        # always remove from output stack
        self.output = []
    
    # pop item
        
    # insert item x into the input stack and return None
    def enqueue(self, x: int) -> None:
        # insert item into input stack
        self.input.append(x)
        
    # peek item from the output stack and return the first integer item
    def peek(self) -> int:
        if len(self.output) > 0:
            # return the last item from the stack, does not remove the item
            return self.output[-1]
        else:
            # copy from input stack and return the last item
            if len(self.input) > 0:
                self.output = self.input
                return self.output[-1]
            else:
                print("Queue empty") # raise exception
    
    # empty stacks / queue
    def emepty(self):
        if len(self.input) ==0 & len(self.output) == 0:
            return 'Error'
        else:
            return 'Non empty queue'
        
            
    def dequeue(self):
        if len(self.output) == 0:
            if len(self.input) > 0:
                # copy input to output stack
                for i in range(len(self.input)):
                    self.output.append(self.input.pop())
                # return from self.output
                return self.output.pop()
            else:
                print("Empty queue")
        else:
            return self.output.pop()
    
        

if __name__ == "__main__":
    
    print("Implementing a Queue using two Stacks")
    
    
    # naive solution testing
    q = Queue()
 
    
    print("Enqueue 23 and 45")       
    q.enqueue(23)
    q.enqueue(45)
    
    print("Input stack: ", q.input)
    print("Output stack: ", q.output)
    
    print("Dequeue the first item")
    q.dequeue()
    # q.dequeue()
    # q.dequeue()
    print("Input stack: ", q.input)
    print("Output stack: ", q.output)
    

    q.enqueue(5)
    q.enqueue(15)
    
    print("Input stack: ", q.input)
    print("Output stack: ", q.output)
    
    q.dequeue()
    print("Input stack: ", q.input)
    print("Output stack: ", q.output)
    
    q.dequeue()
    print("Input stack: ", q.input)
    print("Output stack: ", q.output)
    
    
        
 