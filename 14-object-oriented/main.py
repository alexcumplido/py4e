# Class: template
# Method or message: capability of a class, operations and behaviors
# Field or Attribute: data and properties in a class
# Object or instance: particular instance of a class reated at runtime. Its values and attributes are called state.

# Sample class, lyfe cycle, inheritance
class PartyAnimal:
    def __init__(self, z):
        self.x = 0  
        self.name = z
        print(f"{self.name} constructed")

    def party(self):
        self.x = self.x + 1
        print(f"{self.name} party count, {self.x}")

    # def __del__(self):
    #     print(f"I am destructed, {self.x}")


class FootbalFan(PartyAnimal):
    def __init__(self, nam):
        super().__init__(nam)
        self.points = 0

    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(f"{self.name} points, {self.points}")

print(type(PartyAnimal))
print(dir(PartyAnimal))


s = PartyAnimal("Sally")
j = FootbalFan("Jim")

s.party()
j.party()
j.touchdown()