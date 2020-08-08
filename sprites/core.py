
class Sprite:
    def __init__(self):
        self.Name = Name
        self.Age = Age
        self.Type = "sprite"

    def GetType(self):
        return self.Type

    def SetType(self, Type):
        self.Type = Type

    def __str__(self):
        return "this is the core sprite object"
