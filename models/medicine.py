class Medicine:
    def __init__(self, name, amount_of_life_it_restores):
        self.name = name
        self.amount_of_life_it_restores = amount_of_life_it_restores
    
    def __str__(self):
        return f"{self.name} restaura {self.amount_of_life_it_restores}"