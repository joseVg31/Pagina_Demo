"""
HTML5: Formularios y Elementos Multimedia
Servidor Flask que recibe y valida el formulario de demostración.

Flujo (mismo que se explica en la diapositiva de seguridad):
Input -> Front-End HTML5 -> HTTPS -> Validación Backend -> Base de datos
Aquí implementamos la parte de "Validación Backend": nunca confiamos
solo en el 'required' del HTML, todo se revisa otra vez aquí.
"""

from datetime import datetime
from flask import Flask, render_template, request

app = Flask(__name__)


def validar_formulario(form):
    """Revalida en el servidor lo que el navegador ya validó en el cliente.
    Devuelve (datos_limpios, lista_de_errores)."""
    errores = []
    datos = {}

    # --- email ---
    email = form.get("email", "").strip()
    if "@" not in email or "." not in email.split("@")[-1]:
        errores.append("El correo no tiene un formato válido.")
    datos["email"] = email

    # --- edad ---
    edad_raw = form.get("edad", "")
    try:
        edad = int(edad_raw)
        if edad < 18 or edad > 99:
            errores.append("La edad debe estar entre 18 y 99.")
    except ValueError:
        errores.append("La edad debe ser un número.")
        edad = None
    datos["edad"] = edad

    # --- fecha ---
    fecha_raw = form.get("fecha", "")
    try:
        datetime.strptime(fecha_raw, "%Y-%m-%d")
        datos["fecha"] = fecha_raw
    except ValueError:
        errores.append("La fecha no es válida.")
        datos["fecha"] = None

    # --- color y volumen (no críticos, solo se guardan) ---
    datos["color"] = form.get("color", "#e44d26")
    datos["volumen"] = form.get("volumen", "50")

    return datos, errores


@app.route("/")
def index():
    return render_template("index.html", resultado=None)


@app.route("/enviar", methods=["POST"])
def enviar():
    datos, errores = validar_formulario(request.form)

    archivo = request.files.get("archivo")
    nombre_archivo = archivo.filename if archivo and archivo.filename else None

    if errores:
        # Si el backend encuentra algo inválido (aunque el navegador lo dejó pasar),
        # se vuelve a mostrar el formulario con el error, nunca se procesa a medias.
        return render_template(
            "index.html",
            resultado=None,
            errores=errores,
        ), 400

    resultado = {
        "email": datos["email"],
        "edad": datos["edad"],
        "fecha": datos["fecha"],
        "color": datos["color"],
        "volumen": datos["volumen"],
        "archivo": nombre_archivo,
    }
    return render_template("index.html", resultado=resultado)


if __name__ == "__main__":
    app.run(debug=True)
