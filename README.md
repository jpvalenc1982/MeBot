# MeBot - Tu compañero de bienestar mental

MeBot es un chatbot diseñado para ofrecer apoyo emocional y respuestas relacionadas con el bienestar mental. Es parte de la aplicación **SereneMe**, que busca brindar herramientas y recursos para mejorar la salud mental de los usuarios.

---

## ¿Qué es SereneMe?

**SereneMe** es una plataforma integral diseñada para apoyar a personas que enfrentan desafíos de salud mental. La aplicación se enfoca en cuatro pilares principales:

1. **Chatbot con IA conversacional 🤖**:  
   MeBot, el chatbot de SereneMe, está disponible las 24 horas del día para brindar apoyo emocional, responder preguntas y ofrecer psicoeducación.

2. **Herramientas de autoayuda 🧘‍♂️**:  
   Incluye ejercicios de mindfulness, seguimiento del estado de ánimo y planes de acción personalizados para manejar el estrés, la ansiedad y otros desafíos emocionales.

3. **Conexión con profesionales 👩‍⚕️**:  
   Facilita el acceso a un directorio de terapeutas y psicólogos, así como la posibilidad de agendar teleconsultas.

4. **Comunidad de apoyo 🤝**:  
   Ofrece foros y grupos moderados donde los usuarios pueden compartir experiencias y recibir apoyo mutuo.

---

## ¿Cómo funciona MeBot?

MeBot utiliza **Inteligencia Artificial** para responder preguntas relacionadas con la salud mental. Puedes preguntarle sobre temas como:

- Ansiedad
- Depresión
- Estrés
- Autoestima
- Manejo de emociones

MeBot te proporcionará información útil, consejos prácticos y recursos adicionales para que puedas aprender más sobre el tema.

### Ejemplo de uso:
- **Usuario**: ¿Qué es la ansiedad?  
- **MeBot**: La ansiedad es una respuesta natural del cuerpo al estrés, pero si es excesiva, puede requerir atención profesional. Te recomiendo practicar técnicas de relajación como la respiración profunda o el mindfulness.

---

## Tecnologías utilizadas

MeBot está construido con las siguientes tecnologías:

- **Python**: Lenguaje de programación principal.
- **FastAPI**: Framework para crear la API del servidor.
- **Pandas**: Para manejar y procesar el dataset de preguntas y respuestas.
- **Difflib**: Para encontrar coincidencias entre las preguntas del usuario y el dataset.
- **HTML/CSS/JavaScript**: Para la interfaz de usuario del chatbot.
- **Jinja2**: Para la renderización de plantillas (opcional, si se usa en el futuro).

---

## Estructura del proyecto

El proyecto está organizado de la siguiente manera:

mebot/
├── static/
│ ├── index.html # Interfaz de usuario del chatbot
│ ├── script.js # Lógica del lado del cliente (JavaScript)
│ ├── styles.css # Estilos para la interfaz de usuario
│ └── favicon.ico # Ícono de la aplicación
├── CLA # Términos y condiciones de uso para contribuciones
├── CODE_OF_CONDUCT.md # Código de conducta para contribuciones
├── CONTRIBUTING.md # Pautas para contribuir al proyecto
├── datos_salud_mental_preguntas.csv # Base de datos de preguntas y respuestas
├── LICENSE # Licencia del proyecto MeBot
├── main.py # Lógica del servidor (Python con FastAPI)  
└── README.md # Documentación del proyecto

---

## Instrucciones de uso

Sigue estos pasos para ejecutar MeBot en tu entorno local:

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/mebot.git
   cd mebot
   ```
2. **Instala las dependencias:**:

pip install -r requirements.txt

3. **Ejecuta la aplicación:**:

uvicorn main:app --reload

4. **Abre tu navegador:**:

Visita http://127.0.0.1:8000/ para interactuar con MeBot.

---

## Características clave

- **Interfaz intuitiva:** Diseño limpio y fácil de usar.

- **Respuestas instantáneas:** MeBot responde en tiempo real.

- **Personalización:** Las preguntas y respuestas se adaptan a las necesidades del usuario.

- **Base de datos amplia:** Más de 50 preguntas y respuestas relacionadas con la salud mental.

---

## ¡Contribuye!

¡Tu contribución es bienvenida! Si deseas mejorar MeBot, sigue estos pasos:

Haz un **fork** del repositorio.

Crea una nueva rama: git checkout -b nueva-funcionalidad.

Realiza tus cambios y haz commit: git commit -m "Agrega nueva funcionalidad".

Haz push a la rama: git push origin nueva-funcionalidad.

Abre un **Pull Request**.

Por favor, revisa las [pautas de contribución](CONTRIBUTING.md) antes de enviar tus cambios.

---

## Acuerdo de Licencia de Contribuyente (CLA)

Antes de que tu contribución sea aceptada, deberás firmar nuestro **Acuerdo de Licencia de Contribuyente (CLA)**. Este acuerdo otorga a [SereneMeApp] los derechos de autor y de propiedad intelectual sobre tus contribuciones, mientras que tú conservas los derechos de autor sobre tu trabajo.

Puedes firmar el CLA electrónicamente siguiendo las instrucciones que se te proporcionarán cuando abras un **Pull Request**.

---


## Licencia

Este proyecto está bajo una licencia personalizada que permite contribuciones y uso no comercial, pero restringe el uso comercial. Para más detalles, consulta el archivo [LICENSE](LICENSE).

---

## Contacto

Si tienes preguntas o sugerencias, no dudes en contactarme:

Email: jpvalenc@gmail.com
GitHub: jpvalenc1982
X: @jpvalenc

¡Gracias por usar MeBot! Esperamos que esta herramienta te sea de gran ayuda en tu camino hacia el bienestar mental. 😊
