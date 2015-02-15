# driblando-o-dribbble
Aplicação Django para consultar a Dribbble API

Deve conter
======

- [x] Implementado com responsividade web(Sugestão Bootstrap).
- [x] Lista de shots. Exemplo de chamada na API: http://api.dribbble.com/shots/popular?page=1
- [x] Paginação na tela de lista (aumentando o parâmetro "page").
- [x] Detalhe de um shot. Exemplo de chamada na API: http://api.dribbble.com/shots/1757954
- [x] Tela de detalhe de um shot deve conter autor com foto

Ganha + pontos se acrescentar
======

- [ ] Carregamento assíncrono das imagens e sob demanda
- [ ] Sistema de build e gestão de dependências no projeto.
- [x] Testes no projeto (unitários e por tela).
- [ ] Testes funcionais (que naveguem pela aplicação como casos de uso).
- [ ] Cache de imagens e da API.
- [x] Admin configurado, com algumas customizações.
- [ ] Sinta-se à vontade para incluir features que usem orm e forms, caso queira demonstrar outras habilidades
- [ ] Share em redes sociais.
- [ ] Além do que foi pedido. Nesse caso, só tome cuidado para não fazer uma nova feature que não faça sentido para o produto proposto.

Deploy
======

- [x] Heroku (mas também poderia ser Google App Engine, Digital Ocean, Amazon AWS...)

TODO
======
* Cache
  * https://docs.djangoproject.com/en/1.7/topics/cache/
  * http://www.djangobook.com/en/2.0/chapter15.html
  * http://equallytrue.blogspot.com.br/2012/04/how-to-cache-outgoing-api-calls-in.html

* Testes
  * https://realpython.com/blog/python/testing-in-django-part-1-best-practices-and-examples/
  * http://pythonhosted.org/behave/
  * http://pythontesting.net/start-here/ 
