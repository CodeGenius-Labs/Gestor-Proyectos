// Obtener el botón y el modal
const btnEditar = document.getElementById("btn-editar");
const modal = document.getElementById("modal7");
const closeModal = document.querySelector(".close-btn7");

// Abrir el modal al hacer clic en el botón
btnEditar.addEventListener("click", function() {
    modal.style.display = "block";
});

// Cerrar el modal al hacer clic en el botón de cerrar
closeModal.addEventListener("click", function() {
    modal.style.display = "none";
});

// Cerrar el modal al hacer clic fuera del contenido del modal
window.addEventListener("click", function(event) {
    if (event.target === modal) {
        modal.style.display = "none";
    }
});


// Cuando se hace clic en un botón "Editar", se abre el modal y se cargan los datos
const openModalBtns = document.querySelectorAll('#btn-editar');

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
        const modal = new bootstrap.Modal(document.getElementById('modal7'));
        modal.show();
    });
});

    // Cuando se hace clic en el botón de cerrar, se oculta el modal
    closeModalBtn.addEventListener('click', function() {
        modal.style.display = 'none';
    });

    // Ocultar el modal si se hace clic fuera del contenido del modal
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
 };




 