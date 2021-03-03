"""Python serial number generator."""

class SerialGenerator:
    """serial number generator"""
    def __init__ (self,start):
        self.start = start
        self.newNum = self.start - 1
        

    def generate(self):
        """generates new numbers """
        self.newNum += 1
        print(self.newNum)
        return self.newNum
    
    def reset(self):
        """resets to start"""
        self.newNum = self.start -1
        

    

    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

