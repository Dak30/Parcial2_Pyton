import sqlite3

from flask import Flask, render_template

from pprint import pprint

conexion = sqlite3.connect('web2.sqlite3')
conexion.row_factory = sqlite3.Row
cursor = conexion.cursor()
cursor.execute("""
SELECT * FROM productos;
""")
productos = [dict(producto) for producto in cursor.fetchall()]
pprint(productos)
cursor.close()
conexion.close()

# rutas

app = Flask(__name__)


@app.route('/')
def ruta_raiz():
  return render_template('index.html', productos=productos)
