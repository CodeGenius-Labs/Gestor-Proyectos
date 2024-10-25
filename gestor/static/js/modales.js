// Obtener los botones de "Editar" y el modal
// modal Editar proyecto

const openModalBtns = document.querySelectorAll('.btn-editar'); // Asegúrate de que la clase tenga un punto delante
const modal = document.getElementById('modal7');
const closeModalBtn = document.querySelector('.close-btn7');

// Cuando se hace clic en un botón "Editar", se abre el modal y se cargan los datos
openModalBtns.forEach(btn => {
    btn.addEventListener('click', function() {
        // Obtener los atributos data-* del botón de editar
        const proyectoId = this.getAttribute('data-id');
        const nombre = this.getAttribute('data-nombre');
        const descripcion = this.getAttribute('data-descripcion');
        const fechaInicio = this.getAttribute('data-fecha-inicio');
        const fechaFin = this.getAttribute('data-fecha-fin');

        // Cargar los valores en el modal
        document.getElementById('proyecto_id').value = proyectoId;
        document.getElementById('nombre').value = nombre;
        document.getElementById('descripcion').value = descripcion;
        document.getElementById('fecha_inicio').value = fechaInicio;
        document.getElementById('fecha_fin').value = fechaFin;

        // Mostrar el modal
        modal.style.display = 'block';

        // Asegúrate de eliminar cualquier backdrop adicional
        const backdrops = document.querySelectorAll('.modal-backdrop');
        backdrops.forEach(backdrop => backdrop.remove());
    });
});

// Cuando se hace clic en el botón de cerrar, se oculta el modal
closeModalBtn.addEventListener('click', function() {
    modal.style.display = 'none'; // Ocultar el modal
});

// Ocultar el modal si se hace clic fuera del contenido del modal
window.onclick = function(event) {
    if (event.target === modal) {
        modal.style.display = 'none'; // Ocultar el modal
    }
};



