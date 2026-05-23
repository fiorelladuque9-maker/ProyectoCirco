class Vista:
    def mostrar_menu(self):
        print("\n========== CIRCO ==========")
        print("1. Gestionar Clientes")
        print("2. Gestionar Administradores")
        print("3. Gestionar Servicios")
        print("4. Salir")

    def mostrar_menu_clientes(self):
        print("\n------ CLIENTES ------")
        print("1. Registrar cliente")
        print("2. Listar clientes")
        print("3. Volver")

    def mostrar_menu_administradores(self):
        print("\n------ ADMINISTRADORES ------")
        print("1. Registrar administrador")
        print("2. Listar administradores")
        print("3. Volver")

    def mostrar_menu_servicios(self):
        print("\n------ SERVICIOS ------")
        print("1. Registrar servicio")
        print("2. Listar servicios")
        print("3. Volver")

    def obtener_opcion(self):
        return input("Digite una opcion: ")

    def mostrar_mensaje(self, mensaje):
        print(mensaje)