import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import difflib

app = FastAPI(title="MeBot - Tu compañero de bienestar mental", version="1.1.0")

# Permitir CORS para la conexión con frontend (ejemplo: Figma, localhost, etc.)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes cambiar "*" por la URL de tu frontend en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cargar el dataset
file_path = "datos_salud_mental_preguntas.csv"
df = pd.read_csv(file_path, encoding="utf-8", delimiter=",", quotechar='"', on_bad_lines="skip")

# Verificar que las columnas sean correctas
expected_columns = ["question", "answer"]
if not all(col in df.columns for col in expected_columns):
    raise ValueError(f"El dataset debe contener las columnas {expected_columns}, pero tiene {df.columns.tolist()}.")

# Función para encontrar la respuesta más similar
def encontrar_respuesta(pregunta_usuario: str) -> str:
    preguntas_dataset = df["question"].dropna().tolist()
    mejor_coincidencia = difflib.get_close_matches(pregunta_usuario, preguntas_dataset, n=1, cutoff=0.5)

    if mejor_coincidencia:
        respuesta = df.loc[df["question"] == mejor_coincidencia[0], "answer"].values[0]
        return respuesta
    else:
        return "Lo siento, no tengo una respuesta para esa pregunta. ¿Podrías reformularla?"

@app.get("/", response_class=HTMLResponse)
def home():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <link href="https://fonts.googleapis.com/css?family=Urbanist:wght@500&display=swap" rel="stylesheet">
        <title>MeBot - Chat de Bienestar</title>
        <style>
            body {
                font-family: 'Urbanist', sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: #f7f7f7;
                margin: 0;
            }
            .container {
                width: 100%;
                max-width: 400px;
                padding: 20px;
                background-color: #fff;
                border-radius: 10px;
                box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
                text-align: center;
            }
            h1 {
                color: #333;
                font-size: 22px;
            }
            input, button {
                width: 100%;
                padding: 10px;
                margin-top: 10px;
                border: 1px solid #ddd;
                border-radius: 5px;
            }
            button {
                background-color: #007bff;
                color: white;
                font-size: 16px;
                cursor: pointer;
            }
            button:hover {
                background-color: #0056b3;
            }
            .response {
                margin-top: 15px;
                font-size: 16px;
                color: #444;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>¡Hola! 👋 Soy MeBot</h1>
            <p>Tu compañero de bienestar mental. Escribe una pregunta y te responderé.</p>
            <input type="text" id="pregunta" placeholder="Escribe tu pregunta aquí">
            <button onclick="obtenerRespuesta()">Preguntar</button>
            <div class="response" id="respuesta"></div>
        </div>

        <script>
            async function obtenerRespuesta() {
                let pregunta = document.getElementById("pregunta").value;
                let response = await fetch(`/preguntar/?pregunta=${encodeURIComponent(pregunta)}`);
                let data = await response.json();
                document.getElementById("respuesta").innerText = data.respuesta;
            }
        </script>
    </body>
    </html>
    """
    return html_content
## Función para responder a la pregunta
@app.get("/preguntar/")
def preguntar(pregunta: str):
    respuesta = encontrar_respuesta(pregunta)
    return {"pregunta": pregunta, "respuesta": respuesta}