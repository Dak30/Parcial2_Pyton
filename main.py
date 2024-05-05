from flask import Flask, render_template
import sqlite3
from pprint import pprint
from flask.helpers import redirect

conexion = sqlite3.connect('web2.sqlite3')
conexion.row_factory = sqlite3.Row
cursor = conexion.cursor()
cursor.execute("""
SELECT * FROM productos;
""")
productos = [dict(producto) for producto in cursor.fetchall()]
cursor.close()
conexion.close()

# rutas

app = Flask(__name__)


@app.route('/')
def ruta_raiz():
  return render_template('index.html', productos=productos)


@app.route('/producto/<int:pid>')
def ruta_producto(pid):
  for producto in productos:
    if pid == producto['id']:
      return render_template('producto.html', producto=producto)
  return redirect('/')


#progrma principal

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
