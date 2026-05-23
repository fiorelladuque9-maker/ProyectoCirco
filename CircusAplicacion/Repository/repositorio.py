class Repositorio:
    def __init__(self):
        self.clientes = []
        self.administradores = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def adicionar_administrador(self, administrador):
        self.administradores.append(administrador)

    def listar_clientes(self):
        return self.clientes

    def listar_administradores(self):
        return self.administradores