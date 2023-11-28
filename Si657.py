import flask
from flask import Flask, redirect, url_for, request, jsonify
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Creacion de data
productos = [
          {
        "id": "GGOEGFKA086699",
        "nombre": "Google Home",
        "descripcion": "Asistente Google Home",
        "caracteristicas": "Asistente de voz Google Home para casa",
        "precio": "260",
        "claves": "Asistente, IA, Home, parlante",
        "url": "GoogleHome",
        "categoria": "Tecnologia",
        "subcategoria": "accesorios"
      },
      {
        "id": "GGOEWCKQ085457",
        "nombre": "Nuevo Echo Dot (4ta Generación, Edición 2020)",
        "descripcion": "Nuevo Echo Dot (4ta Generación, Edición 2020)",
        "caracteristicas": "Nuevo echo dot 4a edicion parlante inteligente Alexa",
        "precio": "70.00",
        "claves": "Asistente, IA, Home, parlante",
        "url": "EchoDot",
        "categoria": "Tecnologia",
        "subcategoria": "accesorios"
      },
      {
        "id": "GGOEGHPB071610",
        "nombre": "Echo Pop",
        "descripcion": "Parlante inteligente y compacto con sonido definido y Alexa | versión internacional ",
        "precio": "40.00",
        "claves": "Asistente, IA, Home, parlante",
        "url": "EchoPop",
       "categoria": "Tecnologia",
        "subcategoria": "parlante"
      },
]
usuarios = [
          {
        "id": "001",
        "nombre": "Luis Perez",
              },
       {
        "id": "002",
        "nombre": "Juan Perez",
              },
               {
        "id": "003",
        "nombre": "Ana Perez",
              },
]
@app.route('/api/v1/productos/all', methods=['GET'])
def api_all():
    return jsonify(productos)

@app.route('/api/v1/productos/<string:url>',methods = ['GET'])
def products(url):
    print (url)
    results = []
    for producto in productos:
        print(producto)
        if producto['url'] == url:
            results.append(producto)
    return jsonify(results)

@app.route('/api/v1/usuarios/all', methods=['GET'])
def api_todos():
    return jsonify(usuarios)

@app.route('/api/v1/usuarios/<string:id>',methods = ['GET'])
def users(id):
    print (id)
    results = []
    for usuario in usuarios:
        print(usuario)
        if usuario['id'] == id:
            results.append(usuario)
    return jsonify(results)
@app.route('/api/v1/subcategoria/<string:subcategoria>',methods = ['GET'])
def subcategorias(subcategoria):
    print (subcategoria)
    results = []
    for producto in productos:
        print(producto)
        if producto['subcategoria'] == subcategoria:
            results.append(producto)
    return jsonify(results)

app.run(host='0.0.0.0', port=80)