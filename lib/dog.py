#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    
    def __init__(self, breed='', name=''):
        self.name = name
        self.breed = breed
        

    @property
    def name(self):
        
        return self._name
    
    @name.setter
    def name(self, name):
        if type(name) != str or type(name) == str('') or (1 > len(name) > 25):
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = name
            

    @property 
    def breed(self):
        
        return self._breed
    
    @breed.setter
    def breed(self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print('Breed must be in list of approved breeds.')
            


fido = Dog('Fdfhlsghladjhglkajghlksajhglkasjghlkasjhglkjgh')

