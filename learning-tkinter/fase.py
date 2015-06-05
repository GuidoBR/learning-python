class Fase():
    def __init__(self):
        """
        Inicializador da fase
        """
        self._personagem = []

    def _adicionar_personagem(self, *personagens):
        self._personagem.extend(personagens)

