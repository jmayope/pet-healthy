class Veterinarian:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"
    
    def attendPet(pet, medicine):
        if pet.life + medicine.amount_of_life_it_restores > 100:
            pet.life = 100
        else:
            pet.life += medicine.amount_of_life_it_restores
            
        return pet