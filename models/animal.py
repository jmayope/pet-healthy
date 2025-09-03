class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.life = 100
    
    def __str__(self):
        return f"{self.name} de {self.age} años"

    def emit_sound():
        return "emit sound"