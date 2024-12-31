class Point: # class name should start with capital letter
     
    def __init__(self,x,y):
        self.x=x 
        self.y=y 
        print("constructor")
        
    """
    => This is the constructor method of the class, also known as the __init__ method. The __init__ method is a special method in Python that gets called automatically when a new instance (object) of the class is created.
    => The self parameter refers to the current instance of the class (the object being created). It is used to access instance variables and methods of the object.
    => x and y are the parameters passed when creating a Point object, and they will represent the coordinates of a point.
    
    """    
        
    
    def move(self): # every methid in the class should have the self parameter
        print("move")
    
    def draw(self):
        print("draw")
        
        
point=Point(10,20)

point.x=19 # we can change the value of x

print(point.x)


class Person:
    
    def __init__(self,name):
        self.name=name 
        
    def talk(self):
        print(f"Hi, I am {self.name}")
        

person=Person("John")
person.talk()

ihan=Person("Ihan")
ihan.talk()              