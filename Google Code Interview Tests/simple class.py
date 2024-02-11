###
# Design a class with the following functions:
#   1. Inserting a value into the class (no duplicates)
#   2. Removing a value from the class
#   3. GetRandom a value that is already inserted (with equal probability)

import random

class TestClass:
    def __init__(self):
        self.values = []
        self.map = {}
    
    def insert(self, value):
        if value in self.map:
            return
        
        self.values.append(value)
        self.map[value] = len[self.values]-1
    
    def remove(self, value):
        if value not in self.map:
            return
        
        index = self.map[value]

        self.map.pop(value)

    def getRandom(self):
        randomValue = random.choice(list(self.map))
        print(randomValue)
        return randomValue
    
example = TestClass()
example.insert(3)
example.insert(5)
example.insert(8)
print(example.map)
example.remove(3)
print(example.map)
example.getRandom()