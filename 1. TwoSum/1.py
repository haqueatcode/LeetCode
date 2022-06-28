"""
1. Two sum

Type: Easy
DS: Hashmap
"""

class Twosum:
    def tow_sum(self, data, target):
        # keep visited items in a dictionary
        # if the remaining amount is found in the dictionary
        # return current item and the remaining value
        store = {}
        # for storing multiple pairs if present
        result = []
        for current_number in data:
            if target - current_number in store:
                result.append([target-current_number, current_number])
            
            store[current_number] = target-current_number

        if result:
            return result
        else:
            return "Not found"
                
if __name__ == "__main__":
    
    ts = Twosum()
    
    print(ts.tow_sum([1,2,3,4,5,6,7,8,9], 15))
    # should we print multiple pairs if present?
    
 
    
    
        
        
        
