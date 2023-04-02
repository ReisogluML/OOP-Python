"""
Let's model a couple of actions on our Point class. 
We can start with a method called reset, which moves the point to the origin 
(the origin is the place where x and y are both zero). 
This is a good introductory action because it doesn't require any parameters:
"""

class FirstModel:
    def Model(self) -> int:
        self.first = 0
        self.second = 0

if __name__=="__main__":
    copy = FirstModel()
    copy.Model()
    print(copy.first, copy.second)

