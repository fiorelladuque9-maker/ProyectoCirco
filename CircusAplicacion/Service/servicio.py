class Servico:
    def __init__(self, nome, descripcion, precio):
        self.nome = nome
        self.descripcion = descripcion
        self.precio = precio

    def __str__(self):
        return f"Servicio: {self.nome} | Descripcion: {self.descripcion} | Precio: {self.precio}"