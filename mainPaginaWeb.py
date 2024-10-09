from flask import Flask, render_template, jsonify, request, redirect, url_for

usuarios= [
    {"id":"1", "nombre":"Daniel", "usuario":"dan", "contrasena":"123"}
]

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

#login
@app.route("/acceso-login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        _usuario = request.form["txtUsuario"]
        _contrasena = request.form["txtContrasena"]
        
        # Verificar credenciales
        for user in usuarios:
            if user["usuario"] == _usuario and user["contrasena"] == _contrasena:
                return redirect(url_for("admin"))
        
        # Si las credenciales no son válidas
        return render_template("index.html", error="Usuario o contraseña incorrectos")
    
    return render_template("index.html")

@app.route("/usuarios", methods=["GET"])
def getUsuarios():
    return jsonify(usuarios)

@app.route("/usuarios", methods=["POST"])
def postUsuarios():
    nuevoUsuario=request.json
    usuarios.append(nuevoUsuario)
    return "Producto creado correctamente"

@app.route("/usuarios/<id>", methods=["DELETE"])
def deleteUsuarios(id):
    for user in usuarios:
        if user["id"] == id:
            usuarios.remove(user)
            return f"Producto con id {id} borrado correctamente"
    return "Producto no encontrado"
    
@app.route("/usuarios/<id>", methods=["PUT"])
def editUsuarios(id):
    nuevoUsuario=request.json
    for user in usuarios:
        if user["id"] == id:
            idx=usuarios.index(user)
            usuarios[idx]=nuevoUsuario
            return "Producto editado correctamente"
    return "Producto no encontrado"
app.run()