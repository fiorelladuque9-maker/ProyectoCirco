from Controller.controlador import Controlador
from Repository.repositorio import Repositorio
from View.vista import Vista


def main():
    repositorio = Repositorio()
    vista = Vista()
    controlador = Controlador(repositorio, vista)

    controlador.iniciar()


if __name__ == "__main__":
    main()