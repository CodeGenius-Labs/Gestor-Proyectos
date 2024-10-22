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
