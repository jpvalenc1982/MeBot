import pandas as pd
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import difflib

app = FastAPI(title="MeBot, tu compañero de bienestar mental SereneMe App", version="1.0.0")

# Cargar el dataset
file_path = "datos_salud_mental_preguntas.csv"
df = pd.read_csv(file_path, encoding="utf-8", delimiter=",", quotechar='"')

# Verificar que las columnas sean correctas
expected_columns = ["question", "answer"]
if list(df.columns) != expected_columns:
    raise ValueError(f"El dataset debe contener las columnas {expected_columns}, pero tiene {df.columns.tolist()}.")

# Función para encontrar la pregunta más similar
def encontrar_respuesta(pregunta_usuario: str) -> str:
    preguntas_dataset = df["question"].tolist()
    mejor_coincidencia = difflib.get_close_matches(pregunta_usuario, preguntas_dataset, n=1, cutoff=0.6)

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
        <link href="https://fonts.googleapis.com/css?family=Urbanist:wght@500&display=swap" rel="stylesheet">
        <title>MeBot - Tu compañero de bienestar mental</title>
        <style>
            body {
                font-family: 'Urbanist', sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                background-color: #f0f0f0; /* Un fondo suave */
                margin: 0; /* Elimina márgenes predeterminados */
            }
            .container {
                width: 300px; /* Ajusta el ancho según tus necesidades */
                padding: 20px;
                background-color: #fff; /* Fondo blanco para el contenedor */
                border-radius: 10px; /* Bordes redondeados */
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1); /* Sombra suave */
                text-align: center; /* Centra el texto */
            }
            h1 {
                color: #212121;
                font-size: 24px;
                margin-bottom: 10px;
            }
            p {
                color: #555; /* Texto un poco más oscuro */
                font-size: 16px;
                line-height: 1.6;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>¡Hola! Soy MeBot</h1>
            <p>Tu compañero de bienestar mental. ¿En qué puedo ayudarte hoy?</p>
        </div>
    </body>
    </html>
    """
    return html_content

# Endpoint para obtener una respuesta basada en la pregunta del usuario
@app.get("/preguntar/")
def preguntar(pregunta: str):
    respuesta = encontrar_respuesta(pregunta)
    return {"pregunta": pregunta, "respuesta": respuesta}