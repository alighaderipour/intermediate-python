import os
os.system('cls' if os.name == 'nt' else 'clear')

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    @property
    def 