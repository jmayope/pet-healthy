from typing import List
from .animal import Animal

class Customer:
    def __init__(self, name: str, pets: List[Animal] = None):
        self.name = name
        self.pets = pets

    def __str__(self):
        return f"Cliente: {self.name} - Mascotas: {[pet.name for pet in self.pets]}"

    def add_pet(self, pet: Animal): 
        self.pets.append(pet)
    
    def pet_list(self):
        return self.pets