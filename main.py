from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import pandas as pd
import difflib

# Crear una instancia de FastAPI
app = FastAPI(title="MeBot - Tu compañero de bienestar mental", version="1.1.0")

# Configuración de CORS (para permitir solicitudes desde cualquier origen)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especifica dominios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Servir archivos estáticos (CSS, JS y favicon)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Cargar dataset de preguntas y respuestas
file_path = "datos_salud_mental_preguntas.csv"
df = pd.read_csv(file_path, encoding="utf-8", delimiter=",", quotechar='"', on_bad_lines="skip")

# Verificar que el dataset tenga las columnas esperadas
expected_columns = ["question", "answer"]
if not all(col in df.columns for col in expected_columns):
    raise ValueError(f"El dataset debe contener las columnas {expected_columns}, pero tiene {df.columns.tolist()}.")

# Función para encontrar la mejor respuesta
def encontrar_respuesta(pregunta_usuario: str) -> str:
    preguntas_dataset = df["question"].dropna().tolist()  # Obtener todas las preguntas del dataset
    mejor_coincidencia = difflib.get_close_matches(pregunta_usuario, preguntas_dataset, n=1, cutoff=0.5)  # Buscar la mejor coincidencia
    return df.loc[df["question"] == mejor_coincidencia[0], "answer"].values[0] if mejor_coincidencia else "Lo siento, no tengo una respuesta para esa pregunta. ¿Podrías reformularla?"

# Ruta principal que sirve la página HTML
@app.get("/", response_class=HTMLResponse)
def home():
    with open("static/index.html", "r", encoding="utf-8") as file:
        return HTMLResponse(content=file.read())

# Ruta para manejar las preguntas del usuario
@app.get("/preguntar/")
def preguntar(pregunta: str):
    respuesta = encontrar_respuesta(pregunta)  # Obtener la respuesta
    return {"pregunta": pregunta, "respuesta": respuesta}  # Devolver la respuesta en formato JSON