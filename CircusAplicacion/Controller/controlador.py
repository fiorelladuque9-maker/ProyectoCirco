class Controlador:
    def __init__(self):
        self.clientes = []
        self.administradores = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def adicionar_administrador(self, administrador):
        self.administradores.append(administrador)

    def listar_clientes(self):
        for cliente in self.clientes:
            print(cliente)

    def listar_administradores(self):
        for administrador in self.administradores:
            print(administrador,"holaaaa")