document.addEventListener("DOMContentLoaded", function() {
    const modal3 = document.getElementById('modal3');
    const openModalBtn3 = document.getElementById('openModalBtnModal3');
    const closeModalBtn3 = document.querySelector('.close-btn-modal3');


    // Lógica para abrir el modal
    openModalBtn3.onclick = function () {
        modal3.style.display = 'block';
    }
    
    closeModalBtn3.onclick = function () {
        modal3.style.display = 'none';
    }

    // Cerrar el modal al hacer clic fuera de él
    window.onclick = function (event) {
        if (event.target === modal3) {
            modal3.style.display = 'none';
        }
    }

    window.showFileNameModal3 = function() {
        const input = document.getElementById('legalDocumentModal3');
        const fileName = document.getElementById('file-name-modal3');
        fileName.textContent = input.files.length > 0 ? input.files[0].name : 'No se ha seleccionado ningun archivo';
    }
});
