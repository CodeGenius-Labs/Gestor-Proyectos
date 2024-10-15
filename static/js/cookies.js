document.addEventListener('DOMContentLoaded', () => {
    const botonAceptarCookies = document.getElementById('btn-aceptar-cookies');
    const botonRechazarCookies = document.getElementById('btn-rechazar-cookies'); // Añadir botón de rechazo
    const avisoCookies = document.getElementById('avisocookies');
    const fondoAvisoCookies = document.getElementById('fondoavisocookies');

    // Mostrar modal si no se ha aceptado o rechazado cookies
    if (!localStorage.getItem('cookiesaceptadas')) {
        avisoCookies.classList.add('activo');
        fondoAvisoCookies.classList.add('activo');
    }

    // Aceptar cookies
    botonAceptarCookies.addEventListener('click', () => {
        fondoAvisoCookies.classList.remove('activo');
        avisoCookies.classList.remove('activo');
        localStorage.setItem('cookiesaceptadas', true);
        localStorage.removeItem('cookiesrechazadas'); // Limpiar el rechazo si acepta cookies
    });

    // Rechazar cookies
    botonRechazarCookies.addEventListener('click', () => {
        alert('No puedes usar las funcionalidades de esta plataforma sin aceptar las cookies.'); // Mostrar advertencia
        localStorage.setItem('cookiesrechazadas', true);
        // Mantener visible el modal de cookies para que el usuario pueda decidir de nuevo
        avisoCookies.classList.add('activo');
        fondoAvisoCookies.classList.add('activo');
    });

    // Si las cookies fueron rechazadas previamente, el modal vuelve a aparecer
    if (localStorage.getItem('cookiesrechazadas')) {
        avisoCookies.classList.add('activo');
        fondoAvisoCookies.classList.add('activo');
    }
});
