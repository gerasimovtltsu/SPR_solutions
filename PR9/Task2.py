class Animal:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, breed)
        self.breed_type = "dog"

class Cat(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, breed)
        self.breed_type = "cat"

dog1 = Dog("Barksalot", 4, "Labrador")
cat1 = Cat("Fluffy", 7, "Persian")

print(dog1.name, dog1.breed_type, dog1.breed)
print(cat1.name, cat1.breed_type, cat1.breed)