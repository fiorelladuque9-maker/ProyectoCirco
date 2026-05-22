class Servico:
    def __init__(self, nome, descricao, preco):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco

    def __str__(self):
        return f"Serviço: {self.nome}, Descrição: {self.descricao}, Preço: {self.preco}"