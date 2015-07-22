from animais import Cachorro, Gato, ManadaVirgula, ManadaHifem
import unittest


class CachorroTest(unittest.case.TestCase):
    def setUp(self):
        self.cao = Cachorro()

    def test_cao_deve_latir(self):
        self.assertEqual('Au', self.cao.fazer_barulho())


class GatoTest(unittest.case.TestCase):
    def setUp(self):
        self.gato = Gato()

    def test_gato_deve_miar(self):
        self.assertEqual('Miau', self.gato.fazer_barulho())


class ManadaVirgulaTest(unittest.case.TestCase):
    def setUp(self):
        self.cao = Cachorro()
        self.gato = Gato()
        self.manada = ManadaVirgula([self.cao, self.gato])

    def test_manda_deve_escrever_os_barulhos_dos_animais(self):
        self.assertEqual('Au, Miau', self.manada.fazer_barulho())


class ManadaHifemTest(unittest.case.TestCase):
    def setUp(self):
        self.cao = Cachorro()
        self.gato = Gato()
        self.manada = ManadaHifem([self.cao, self.gato])

    def test_manda_deve_escrever_os_barulhos_dos_animais(self):
        self.assertEqual('Au - Miau', self.manada.fazer_barulho())

if __name__ == '__main__':
    unittest.main()
