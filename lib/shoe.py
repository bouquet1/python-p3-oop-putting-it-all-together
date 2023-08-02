#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size, condition = None):
        self.brand = brand
        self.size = size
        self._condition = condition

    def get_size(self):
        return self._size
 
    def set_size(self,size):
        if not isinstance(size, int):
            print("size must be an integer")
        else: 
            self._size = size
        
    size = property(get_size, set_size)

    @property
    def condition(self):
        return self._condition

    def cobble(self):
        print("Your shoe is as good as new!")
        # Set the condition to "New"
        self._condition = "New"


# try python lib/shoe.py to check
stan_smith = Shoe("Adidas", 9)
stan_smith.cobble()
print(stan_smith.condition)

  

