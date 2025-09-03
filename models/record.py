class Record:
    def __init__(self, detail: str, created_at: str):
        self.detail = detail
        self.created_at = created_at

    def __str__(self):
        return f"Registro: <{self.detail}> - Fecha: {self.created_at}"