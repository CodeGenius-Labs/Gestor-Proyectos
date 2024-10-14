const modal = document.getElementById('modal');
        const openModalBtn = document.getElementById('openModalBtn');
        const closeModalBtn = document.querySelector('.close-btn');
        const closeButton = document.getElementById('closeModalBtn'); 
        
        // Abre el modal 
        openModalBtn.onclick = function() {
            modal.style.display = 'block';
        }
        
        // Cierra el modal
        closeModalBtn.onclick = function() {
            modal.style.display = 'none';
        }

        // Cierra el modal al hacer clic fuera de él
        window.onclick = function(event) {
            if (event.target == modal) {
                modal.style.display = 'none';
            }
        }
