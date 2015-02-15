# -*- coding: utf-8 -*-
import requests as req


class Dribbble():
    url = 'http://api.dribbble.com/'

    def __str__(self):
        return 'Dribbble'

    def getUrlPopular(self, page=''):
        return self.url + 'shots/popular?page=' + str(page)

    def getUrlShotById(self, id):
        return self.url + 'shots/' + str(id)

    def getPopular(self, page=''):
        r = req.get(self.getUrlPopular(page))
        json = r.json()
        return json['shots']

    def getInformacoesShotPopulares(self, page=''):
        dic_shot = {}
        lista_shots = []
        json = self.getPopular(page)
        for shot in json:
            completo = self.getImagemEAutor(shot['id'])
            dic_shot = {
                'id': shot['id'],
                'title': shot['title'],
                'description': shot['description'],
                'url': shot['url'],
                'imagem': completo['imagem'],
                'autor': completo['autor'],
            }
            lista_shots.append(dic_shot)
        return lista_shots

    def getImagemEAutor(self, id):
        json = self.getDetalhesShot(id)
        return {'imagem': json['image_url'], 'autor': json['player']['name']}

    def getDetalhesShot(self, id):
        r = req.get(self.getUrlShotById(id))
        return r.json()
