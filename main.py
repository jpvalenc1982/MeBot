from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import pandas as pd
import difflib

app = FastAPI(title="MeBot - Tu compañero de bienestar mental", version="1.1.0")

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especifica dominios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Servir archivos estáticos (CSS y JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Cargar dataset
file_path = "datos_salud_mental_preguntas.csv"
df = pd.read_csv(file_path, encoding="utf-8", delimiter=",", quotechar='"', on_bad_lines="skip")

# Verificar columnas
expected_columns = ["question", "answer"]
if not all(col in df.columns for col in expected_columns):
    raise ValueError(f"El dataset debe contener las columnas {expected_columns}, pero tiene {df.columns.tolist()}.")

# Función para encontrar la mejor respuesta
def encontrar_respuesta(pregunta_usuario: str) -> str:
    preguntas_dataset = df["question"].dropna().tolist()
    mejor_coincidencia = difflib.get_close_matches(pregunta_usuario, preguntas_dataset, n=1, cutoff=0.5)
    return df.loc[df["question"] == mejor_coincidencia[0], "answer"].values[0] if mejor_coincidencia else "Lo siento, no tengo una respuesta para esa pregunta. ¿Podrías reformularla?"

@app.get("/", response_class=HTMLResponse)
def home():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <link rel="stylesheet" href="/static/styles.css">
        <title>MeBot - Chat de Bienestar</title>
    </head>
    <body>
        <div class="container">
            <h1>¡Hola! 👋 Soy MeBot</h1>
            <p>Tu compañero de bienestar mental. Escribe una pregunta y te responderé.</p>
            <input type="text" id="pregunta" placeholder="Escribe tu pregunta aquí">
            <button onclick="obtenerRespuesta()">Preguntar</button>
            <div id="historial"></div>
        </div>
        <script src="/static/script.js"></script>
    </body>
    </html>
    """
    return html_content

@app.get("/preguntar/")
def preguntar(pregunta: str):
    respuesta = encontrar_respuesta(pregunta)
    return {"pregunta": pregunta, "respuesta": respuesta}