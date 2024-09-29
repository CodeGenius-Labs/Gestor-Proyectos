document.addEventListener("DOMContentLoaded", function() {
    const modal2 = document.getElementById('modal2');
    const openModalBtn2 = document.getElementById('openModalBtn2'); 
    const closeModalBtn2 = document.getElementById('closeModalBtn2'); 

    openModalBtn2.onclick = function() {
        modal2.style.display = 'block';
    }

    closeModalBtn2.onclick = function() {
        modal2.style.display = 'none';
    }

    // Cierra el modal al hacer clic fuera de él
    window.onclick = function(event) {
        if (event.target === modal2) {
            modal2.style.display = 'none';
        }
    }

    decrementButton2.onclick = function() {
        let currentValue = parseInt(numberInput2.value);
        if (currentValue > parseInt(numberInput2.min)) {
            numberInput2.value = currentValue - 1;
        }
    }
    
    incrementButton2.onclick = function() {
        let currentValue = parseInt(numberInput2.value);
        if (currentValue < parseInt(numberInput2.max)) {
            numberInput2.value = currentValue + 1;
        }
    }
});

