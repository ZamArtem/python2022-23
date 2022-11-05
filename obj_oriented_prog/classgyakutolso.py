
class Person:
    def __init__(self, age, weight, height, first_name, last_name, catch_phrase):
        self.age            = age
        self.weight         = weight
        self.height         = height
        self.first_name     = first_name
        self.last_name      = last_name
        self.catch_phrase   = catch_phrase


user = Person(25, 80, 180, "John", "Snow", "You know nothing, John Snow")


class Liquid:
    def __init__(self,color: None, alcohol: False, clarity: int(), drinkable: True):
        self.color      = color
        self.alcohol    = alcohol
        self.clarity    = clarity
        self.drinkable  = drinkable



water       = Liquid(None,False,7,True)
votka       = Liquid(None,True,8,True)
whisky      = Liquid("Brown",True,4,True)
dirty_water = Liquid("Brown", False, 0, "aha")

