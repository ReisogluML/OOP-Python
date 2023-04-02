"""
We don't have to do anything special in the class definition to be able to add attributes.
We can set arbitrary attributes on an instantiated object using dot notation.
"""

class Attribute:
    pass

first = Attribute()
second = Attribute()

first.x = 1
first.y = 2
second.x = 3
second.y = 4

if __name__=="__main__":
    print(first.x, second.x)
    print(first.y, second.y)
