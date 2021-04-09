import os

class C:
    def something(self):
      print("Hey there!")
    
    def something_else(self):
        self.something()
        x = list([str(r) for r in range(1, 20)])
