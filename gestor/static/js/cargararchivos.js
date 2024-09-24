document.addEventListener("DOMContentLoaded", function() {
    const modal3 = document.getElementById('modal3');
    const openModalBtn3 = document.getElementById('openModalBtn3');
    const closeModalBtn = document.querySelector('.close-btn');

    // Lógica para abrir el modal
    openModalBtn3.onclick = function () {
        modal3.style.display = 'block';
    }
    
    closeModalBtn.onclick = function () {
        modal3.style.display = 'none';
    }

    // Cerrar el modal al hacer clic fuera de él
    window.onclick = function (event) {
        if (event.target === modal3) {
            modal3.style.display = 'none';
        }
    }

    function showFileName() {
        const input = document.getElementById('legalDocument');
        const fileName = document.getElementById('file-name');
        fileName.textContent = input.files.length > 0 ? input.files[0].name : 'No se ha seleccionado ningun archivo';
    }
});
