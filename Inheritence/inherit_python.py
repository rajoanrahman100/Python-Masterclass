class Mammal:
    
    def __init__(self,name):
        self.name=name
        
    def walk(self):
        print(f"{self.name} is walking")
        

class Dog(Mammal): # Dog class is inheriting Mammal class
    pass # pass keyword is used to avoid error when we have empty class

class Cat(Mammal): # Cat class is inheriting Mammal class
    
    def __init__(self,name,breed):
        super().__init__(name) # we are calling the constructor of Mammal class
        self.breed=breed
    

    def meow(self):
        print(f"{self.name} is meowing. The breed is {self.breed}")



dog=Dog("Dog")
dog.walk()

cat=Cat("Katrina","Persian Cat")
cat.walk()
cat.meow()
 