class Animal:
    def __init__(self, species, sound):
        self.species = species
        self.sound = sound

cat = Animal("cat", "meow")
dog = Animal("dog", "woof")

print("Cat:", cat.species, "meows.")
print("Dog:", dog.species, "barks.")
