async function obtenerRespuesta() {
    let preguntaInput = document.getElementById("pregunta");
    let pregunta = preguntaInput.value;
    if (!pregunta.trim()) return;

    let response = await fetch(`/preguntar/?pregunta=${encodeURIComponent(pregunta)}`);
    let data = await response.json();

    let historial = document.getElementById("historial");
    let nuevoMensaje = document.createElement("p");
    nuevoMensaje.innerHTML = `<strong>Tú:</strong> ${pregunta}<br><strong>MeBot:</strong> ${data.respuesta}`;
    historial.appendChild(nuevoMensaje);

    preguntaInput.value = "";
}
