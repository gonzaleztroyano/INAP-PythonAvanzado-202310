from flask import Flask

app = Flask(__name__)


@app.route('/mensaje/saludo')
def saludo():
    return '<h2>Bienvenido a mi primera página web<h2/>'


@app.route('/')
def hola():
    return 'Mi primer programa Flask!'

@app.route("/articulos/<id>")
def mostrar_ariculo(id):
    return 'Vamos a mostrar el artículo con id: {}'.format(id)


if __name__ == '__main__':
    app.run()
