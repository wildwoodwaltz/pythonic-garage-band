
from abc import abstractclassmethod, abstractmethod


class  Band():
    pass

class Musician():
    pass


class Guitarist(Musician):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play guitar" 

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"



class Bassist(Musician):
    pass

class Drummer(Musician):
    
    def __init__(self, name):
        self. name = name

    def __str__(self):
        return f"My name is {self.name} and I play drums" 
    
    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"