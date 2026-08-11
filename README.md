# HTML5: Formularios y Elementos Multimedia — Demo con Flask

Proyecto de demostración para el curso Tecnología Digital Web.
El formulario se valida en el navegador (HTML5) y otra vez en el
servidor (Flask), como se explica en la parte de seguridad del informe.

## Cómo ejecutarlo

```bash
pip install -r requirements.txt
python app.py
```

Luego abre http://127.0.0.1:5000 en el navegador.

## Estructura

- `app.py` — servidor Flask: ruta `/` (muestra el formulario) y
  ruta `/enviar` (POST, valida los datos y responde).
- `templates/index.html` — la página, como plantilla Jinja2.
- `static/` — CSS, JS, video, audio e imágenes.

## Flujo de datos

Usuario llena el formulario → HTML5 valida en el cliente →
POST a `/enviar` → Flask valida otra vez en el servidor →
respuesta de éxito o de error.
