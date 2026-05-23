class Repositorio:
    def __init__(self):
        self.clientes = []
        self.administradores = []
        self.servicios = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def adicionar_administrador(self, administrador):
        self.administradores.append(administrador)

    def adicionar_servicio(self, servicio):
        self.servicios.append(servicio)

    def listar_clientes(self):
        return self.clientes

    def listar_administradores(self):
        return self.administradores

    def listar_servicios(self):
        return self.servicios