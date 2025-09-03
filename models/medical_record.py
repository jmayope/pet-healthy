from typing import List
from .animal import Animal
from .record import Record

class MedicalRecord:
    def __init__(self, code: str, pet: Animal, records: List[Record] = None):
        self.code = code
        self.pet = pet
        self.records = records
    
    def __str__(self):
        return f"Historia clinida #{self.code} de {self.pet.name} - Cantidad de Registros: {len(self.records)}"
    
    def add_record(self, record: Record):
        self.records.append(record)
    