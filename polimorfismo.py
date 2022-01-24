
class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def avanzar(self):
        print('Ando caminando')


class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)

    def avanzar(self):
        print('Ando movimiendome en mi bicicleta')


def main():
    persona = Persona('Rogelio')
    persona.avanzar()

    ciclista = Ciclista('Esmeralda')
    ciclista.avanzar()
    
if __name__ == '__main__':
    main()            