import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session

from ayuda import apology

#configure application
app = Flask(__name__)


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# cs50 library to use SQLite
db = SQL("sqlite:///juegouno.db")


@app.after_request
def after_request(response):
     """Ensure responses aren't cached"""
     response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
     response.headers["Expires"] = 0
     response.headers["Pragma"] = "no-cache"
     return response

@app.route("/")
def index():

    #obtener todos los datos de los jugadores ingresados por el usuario en la ventana para agregar jugadores
    jugadores = db.execute("SELECT * FROM juego")

    for jugador in jugadores:
        puntos  = db.execute(f"SELECT SUM(ronda1 + ronda2 + ronda3 + ronda4 + ronda5 + ronda6 + ronda7 + ronda8 + ronda9 + ronda10) AS total_puntos FROM juego WHERE nombre = ?",
                                    (jugador["nombre"]))[0]["total_puntos"]
        jugador["puntos"] = puntos
        print(f"valor de puntos: {puntos}")

    return render_template('juego.html', jugadores=jugadores)


@app.route("/nueva_partida")
def nueva_partida():

    db.execute("DELETE FROM juego")
    session.clear()

    return redirect("/jugadores")

@app.route("/nueva_partida_jugadores")
def nueva_partida_jugadores():
    jugadores = db.execute("SELECT * FROM juego")
    for jugador in jugadores:
        nombre = jugador['nombre']
        puntos = 0
        for i in range(1,10):
            db.execute(f"UPDATE juego SET ronda{i} = ? WHERE nombre = ?",
                       puntos, nombre)

    return redirect("/")

@app.route("/jugadores", methods=['GET', "POST"])
def jugadores():
    ## indica la cantidad de jugadores agregados a la lista
    jugadores = db.execute("SELECT nombre FROM juego ORDER BY nombre ASC")
    cantidad = len(jugadores)

    if request.method == "POST":
        # asegura que se ha agregado un nombre:
        if not request.form.get("nombre"):
            return apology("debes agregar el nombre de un jugador")

        nombre = request.form.get("nombre").upper()
        # Query database for username
        rows = db.execute(
            "SELECT * FROM juego WHERE nombre = ?",
            nombre
        )
        # Ensure username doesn't exists
        if len(rows) != 0:
            return apology("Ese jugador ya existe.")

        # agregar jugadores a la DB
        i = 0
        db.execute("INSERT INTO juego (nombre, ronda1, ronda2, ronda3, ronda4, ronda5, ronda6, ronda7, ronda8, ronda9, ronda10) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                       nombre, i, i, i, i, i, i, i, i, i, i)

        ## indica que se ha agregado a la lista de jugadores
        flash(f"Se ha agregado a {nombre} a la lista")
        cantidad += 1
        jugadores = db.execute("SELECT nombre FROM juego ORDER BY nombre ASC")

        return render_template("jugadores.html", cantidad = cantidad, jugadores = jugadores)
    else:
        return render_template("jugadores.html",
                               cantidad = cantidad, jugadores=jugadores)

@app.route("/juego", methods=["GET", "POST"])
def juego():
    if request.method == 'POST':
            puntos_totales = []
            for i in range(1, 10):
                sum = db.execute(f"SELECT AVG(ronda{i}) FROM juego")
                print(f"sum:{sum}")
                if sum[0][f'AVG(ronda{i})'] == 0.0:
                    numero_ronda = i
                    print(f"ronda dentro del loop {numero_ronda}")
                    break
            print(f"Valor completo de 'numero_ronda' post for loop: {numero_ronda}")

            for jugador in request.form:
                print(f"Valor completo de 'jugador': {jugador}")  # Imprimir el valor completo de 'jugador'
                if jugador.startswith('puntos_'):
                    jugador_nombre = jugador.split('_')[1]
                    print(f"Valor completo de 'jugador_nombre': {jugador_nombre}")
                    puntos_nueva_ronda = int(request.form[jugador])
                    print(f"Valor completo de 'puntos en la nueva ronda': {puntos_nueva_ronda}")

                    ## agregamos los puntos de la respectiva ronda
                    db.execute(f"UPDATE juego SET ronda{numero_ronda} = ronda{numero_ronda} + ? WHERE nombre = ?",
                                puntos_nueva_ronda, jugador_nombre)

                    for i in range(1, 10):
                        ronda = db.execute(f"SELECT ronda{i} AS puntos FROM juego WHERE nombre = ?",
                                           jugador_nombre)[0]["puntos"]
                        print(f"Ronda{i}: {ronda}")
                    # sumamos los puntos
                    puntos = db.execute(f"SELECT SUM(ronda1 + ronda2 + ronda3 + ronda4 + ronda5 + ronda6 + ronda7 + ronda8 + ronda9 + ronda10) AS total_puntos FROM juego WHERE nombre = ?",
                                    (jugador_nombre))[0]["total_puntos"]
                    puntos_totales.append(puntos)
                    print(f"los puntos de {jugador_nombre} son {puntos}")

                    for puntos in puntos_totales:

                        if puntos >= 200:
                            flash(f"Alguien ha alcanzado o superado los 200 puntos. El juego ha terminado.")

                                #obtener todos los datos de los jugadores ingresados por el usuario en la ventana para agregar jugadores
                            jugadores = db.execute("SELECT * FROM juego")
                            for jugador in jugadores:
                                puntos  = db.execute(f"SELECT SUM(ronda1 + ronda2 + ronda3 + ronda4 + ronda5 + ronda6 + ronda7 + ronda8 + ronda9 + ronda10) AS total_puntos FROM juego WHERE nombre = ?",
                                    (jugador["nombre"]))[0]["total_puntos"]
                                jugador["puntos"] = puntos

                            return render_template("finjuego.html", jugadores = jugadores)

            return redirect("/")
    else:
        return render_template("juego.html")

@app.route("/ganador")
def ganador():
        jugadores = db.execute("SELECT * FROM juego")

        min = 200
        nombre = "nombre"
        for jugador in jugadores:
            puntos  = db.execute(f"SELECT SUM(ronda1 + ronda2 + ronda3 + ronda4 + ronda5 + ronda6 + ronda7 + ronda8 + ronda9 + ronda10) AS total_puntos FROM juego WHERE nombre = ?",
                                    (jugador["nombre"]))[0]["total_puntos"]
            if puntos < min:
                min = puntos
                nombre = jugador["nombre"]
        ## se agrega el ganadore a la base de datos
        flash(f"¡{nombre} ha ganado con {puntos} y se ha agregado a la lista de ganadores!")

        db.execute("INSERT INTO ganadores (nombre, puntos) VALUES (?, ?)",
                                           nombre, min)
        ganadores = db.execute("SELECT * FROM ganadores ORDER BY puntos ASC")

        return render_template("ganadores.html", ganadores = ganadores)


@app.route("/ganadores")
def ganadores():

    ganadores = db.execute("SELECT * FROM ganadores ORDER BY puntos ASC")

    return render_template("ganadores.html", ganadores = ganadores)

@app.route("/reglas")
def reglas():
    ## simplemente ve a la tapu página, please

    return render_template("reglas.html")
