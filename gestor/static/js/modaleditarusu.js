// Obtener todos los botones de editar
document.querySelectorAll('.btn-editar').forEach(function(btn) {
    btn.addEventListener('click', function() {
        var modal = document.getElementById('modal8');
        modal.style.display = 'block';

        // Obtener y cargar los datos del usuario en el modal
        document.getElementById('user_id').value = this.getAttribute('data-id');
        document.getElementById('username').value = this.getAttribute('data-username');
        document.getElementById('email').value = this.getAttribute('data-email');
    });
});

// Cerrar el modal al hacer clic en el botón de cerrar
document.querySelector('.closeModalBtn8').addEventListener('click', function() {
    document.getElementById('modal8').style.display = 'none';
});

// Ocultar el modal si se hace clic fuera del contenido del modal
window.onclick = function(event) {
    var modal = document.getElementById('modal8');
    if (event.target == modal) {
        modal.style.display = 'none';
    }
};