    // Obtener los botones de "Editar" y el modal
    const openModalBtns = document.querySelectorAll('.openModalBtn7');
    const modal = document.getElementById('modal7');
    const closeModalBtn = document.querySelector('.close-btn7');


    const modal7 = document.getElementById('modal7');
    const openModalBtn7 = document.getElementById('openModalBtn7');
    const closeModalBtn7 = document.querySelector('.close-btn7');
    const closeButton7 = document.getElementById('closeModalBtn7'); 
    
    // Abre el modal 
    openModalBtn7.onclick = function() {
        modal7.style.display = 'block';
    }
    
    // Cierra el modal
    closeModalBtn7.onclick = function() {
        modal7.style.display = 'none';
    }
    
    // Cierra el modal al hacer clic fuera de él
    window.onclick = function(event) {
        if (event.target == modal7) {
            modal7.style.display = 'none';
        }
    }






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