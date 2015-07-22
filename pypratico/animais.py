class Animal():
    def fazer_barulho(self):
        return self.barulho


class Cachorro(Animal):
    def __init__(self):
        self.barulho = 'Au'


class Gato(Animal):
    def __init__(self):
        self.barulho = 'Miau'


class Manada():
    def __init__(self, lista_animais):
        self.animais = lista_animais

    def fazer_barulho(self):
        return self.separador.join(
            [animal.fazer_barulho() for animal in self.animais]
        )


class ManadaVirgula(Manada):
    def __init__(self, lista_animais):
        super().__init__(lista_animais)
        self.separador = ', '


class ManadaHifem(Manada):
    def __init__(self, lista_animais):
        super().__init__(lista_animais)
        self.separador = ' - '
