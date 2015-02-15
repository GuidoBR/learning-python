from django.test import TestCase
from driblando.app.models import Autor, Shot
from driblando.app.api import Dribbble


class AutorTestCase(TestCase):
    def setUp(self):
        Autor.objects.create(nome="Guido", foto="img.jpg")

    def test_autor_tem_nome(self):
        autor = Autor.objects.get(nome="Guido")
        self.assertEqual(str(autor), 'Guido')


class ShotTestCase(TestCase):
    def setUp(self):
        tolkien = Autor.objects.create(nome="Tolkien")
        Shot.objects.create(titulo="O Hobbit", autor=tolkien)

    def test_shot_tem_titulo_com_nome_autor(self):
        shot = Shot.objects.get(titulo="O Hobbit")
        self.assertEqual(str(shot), 'O Hobbit - por Tolkien')


class ApiTestCase(TestCase):
    obj = Dribbble()

    def test_nome_da_api(self):
        self.assertEquals(str(self.obj), 'Dribbble')

    def test_retorna_url_shots_recentes(self):
        self.assertEquals(
            self.obj.getUrlPopular(),
            'http://api.dribbble.com/shots/popular?page='
        )

    def test_retorna_url_shots_recentes_paginado(self):
        self.assertEquals(
            self.obj.getUrlPopular(42),
            'http://api.dribbble.com/shots/popular?page=42'
        )

    def test_retorna_url_shots_por_id(self):
        self.assertEquals(
            self.obj.getUrlShotById(1757954),
            'http://api.dribbble.com/shots/1757954'
        )

    def test_retorna_lista_com_shots_populares(self):
        self.assertEquals(
            type(self.obj.getPopular()),
            type([])
        )

    def test_retorna_dicionario_com_15_shots(self):
        self.assertEquals(
            len(self.obj.getPopular()),
            15
        )

    def test_retorna_dicionario_somente_com_informacoes_importantes(self):
        info_importante = {
            'id': '',
            'title': '',
            'description': '',
            'url': '',
            'autor': '',
            'imagem': '',
        }

        for (i, dic) in enumerate(self.obj.getInformacoesShotPopulares()):
            self.assertEquals(
                dic.keys(),
                info_importante.keys()
            )

    def test_retorna_lista_de_dicionario_com_15_shots(self):
        self.assertEquals(
            len(self.obj.getInformacoesShotPopulares()),
            15
        )

    def test_detalhes_shot_e_um_dicionario(self):
        retorno_api = self.obj.getDetalhesShot(1757954)
        self.assertEquals(
            type(retorno_api),
            type({})
        )
