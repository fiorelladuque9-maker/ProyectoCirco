from Model.cliente import Cliente
            elif opcion == "2":
                clientes = self.repositorio.listar_clientes()

                if len(clientes) == 0:
                    self.vista.mostrar_mensaje("No hay clientes registrados")
                else:
                    for cliente in clientes:
                        print(cliente)

            elif opcion == "3":
                self.vista.mostrar_mensaje("Volviendo al menu principal")
            else:
                self.vista.mostrar_mensaje("Opcion invalida")

    def menu_administradores(self):
        opcion = ""

        while opcion != "3":
            self.vista.mostrar_menu_administradores()
            opcion = self.vista.obtener_opcion()

            if opcion == "1":
                nombre = input("Nombre del administrador: ")
                email = input("Email del administrador: ")
                telefono = input("Telefono del administrador: ")

                administrador = Administrador(nombre, email, telefono)
                self.repositorio.adicionar_administrador(administrador)

                self.vista.mostrar_mensaje("Administrador registrado correctamente")

            elif opcion == "2":
                administradores = self.repositorio.listar_administradores()

                if len(administradores) == 0:
                    self.vista.mostrar_mensaje("No hay administradores registrados")
                else:
                    for administrador in administradores:
                        print(administrador)

            elif opcion == "3":
                self.vista.mostrar_mensaje("Volviendo al menu principal")
            else:
                self.vista.mostrar_mensaje("Opcion invalida")

    def menu_servicios(self):
        opcion = ""

        while opcion != "3":
            self.vista.mostrar_menu_servicios()
            opcion = self.vista.obtener_opcion()

            if opcion == "1":
                nombre = input("Nombre del servicio: ")
                descripcion = input("Descripcion del servicio: ")
                precio = input("Precio del servicio: ")

                servicio = Servico(nombre, descripcion, precio)
                self.repositorio.adicionar_servicio(servicio)

                self.vista.mostrar_mensaje("Servicio registrado correctamente")

            elif opcion == "2":
                servicios = self.repositorio.listar_servicios()

                if len(servicios) == 0:
                    self.vista.mostrar_mensaje("No hay servicios registrados")
                else:
                    for servicio in servicios:
                        print(servicio)

            elif opcion == "3":
                self.vista.mostrar_mensaje("Volviendo al menu principal")
            else:
                self.vista.mostrar_mensaje("Opcion invalida")