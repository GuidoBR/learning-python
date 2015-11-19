from bottle import route, run


@route('/<name>')
def index(name):
    return('Hello World, {}!'.format(name))

run(host='localhost', port=8080)
