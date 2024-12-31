class Point: # class name should start with capital letter
     
    
    def move(self):
        print("move")
    
    def draw(self):
        print("draw")
        
        
point=Point()

try:
    print(point.x) # it will give error because we have not defined x in class
except AttributeError:
    print("AttributeError")    

point.draw()
point.move()            