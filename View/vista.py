class Vista:
    def mostrar_menu(self):
        print("Bem-vindo ao Circo!")
        print("1. Gerenciar Clientes")
        print("2. Gerenciar Administradores")
        print("3. Gerenciar Serviços")
        print("4. Sair")

    def obter_opcao(self):
        return input("Escolha uma opção: ")

    def mostrar_mensagem(self, mensagem):
        print(mensagem)