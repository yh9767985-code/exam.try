print("murat can")


student = {"name": "Murat", "age": 24} 
print("Student:", student)


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species


animals = []
names = ["Leo", "Milo", "Rocky", "Nemo", "Kiki"]
species = ["Lion", "Cat", "Dog", "Fish", "Bird"]

for i in range(5):
    animals.append(Animal(names[i], species[i]))


print("\nAnimals:")
for a in animals:
    print(a.name, "-", a.species)
