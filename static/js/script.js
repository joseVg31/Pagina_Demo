// Validación visual en vivo (bordes rojo/verde ya los maneja el CSS con :valid/:invalid).
// Aquí solo evitamos el envío si el navegador detecta campos inválidos;
// si todo es válido, el formulario SÍ se envía de verdad al servidor Flask.
const form = document.getElementById('demoForm');
const status = document.getElementById('formStatus');

form.addEventListener('submit', function (e) {
  if (!form.checkValidity()) {
    e.preventDefault();
    status.textContent = '✗ Hay campos inválidos. Revisa los bordes en rojo.';
    status.classList.remove('ok');
    form.reportValidity();
  }
  // si es válido, no se hace preventDefault: el navegador envía el POST real a Flask
});
