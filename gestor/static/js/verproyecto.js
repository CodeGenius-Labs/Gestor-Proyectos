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



        const decrementButton = document.querySelector('.decrement');
        const incrementButton = document.querySelector('.increment');
        const numberInput = document.getElementById('customNumberInput');
        
        
        decrementButton.onclick = function() {
            let currentValue = parseInt(numberInput.value);
            if (currentValue > parseInt(numberInput.min)) {
                numberInput.value = currentValue - 1;
            }
        }
        
        incrementButton.onclick = function() {
            let currentValue = parseInt(numberInput.value);
            if (currentValue < parseInt(numberInput.max)) {
                numberInput.value = currentValue + 1;
            }
        }