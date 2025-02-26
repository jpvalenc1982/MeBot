// Obtener el campo de texto y el botón
let preguntaInput = document.getElementById("pregunta");
let botonPreguntar = document.querySelector("button");

// Función para obtener la respuesta
async function obtenerRespuesta() {
    let pregunta = preguntaInput.value.trim(); // Elimina espacios en blanco al inicio y final
    if (!pregunta) {
        alert("Por favor, escribe una pregunta."); // Mensaje si el campo está vacío
        return;
    }

    try {
        // Agregar la pregunta del usuario al historial
        let historial = document.getElementById("historial");
        let preguntaUsuario = document.createElement("div");
        preguntaUsuario.className = "pregunta-usuario"; // Clase para estilo de pregunta
        preguntaUsuario.textContent = pregunta; // Texto de la pregunta
        historial.appendChild(preguntaUsuario); // Agrega la pregunta al historial

        // Obtener la respuesta del servidor
        let response = await fetch(`/preguntar/?pregunta=${encodeURIComponent(pregunta)}`);
        let data = await response.json();

        // Agregar la respuesta de MeBot al historial
        let respuestaMeBot = document.createElement("div");
        respuestaMeBot.className = "respuesta-mebot"; // Clase para estilo de respuesta
        respuestaMeBot.textContent = data.respuesta; // Texto de la respuesta
        historial.appendChild(respuestaMeBot); // Agrega la respuesta al historial

        preguntaInput.value = ""; // Limpiar el campo de texto después de enviar la pregunta
    } catch (error) {
        console.error("Error al obtener la respuesta:", error);
        alert("Hubo un error al procesar tu pregunta. Inténtalo de nuevo.");
    }
}

// Escuchar el clic en el botón "Preguntar"
botonPreguntar.addEventListener("click", obtenerRespuesta);

// Escuchar la tecla "Enter" en el campo de texto
preguntaInput.addEventListener("keydown", function (event) {
    if (event.key === "Enter") { // Si la tecla presionada es "Enter"
        event.preventDefault(); // Evitar el comportamiento por defecto (como enviar un formulario)
        obtenerRespuesta(); // Llamar a la función para obtener la respuesta
    }
});