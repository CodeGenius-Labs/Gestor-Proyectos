
    // Evita que el menú principal se cierre al hacer clic en el submenú
    document.querySelectorAll('.dropdown-submenu .dropdown-toggle').forEach(function (element) {
        element.addEventListener('click', function (e) {
            if (!element.nextElementSibling.classList.contains('show')) {
                element.closest('.dropdown-menu').querySelectorAll('.show').forEach(function (dropdown) {
                    dropdown.classList.remove('show');
                });
            }
            element.nextElementSibling.classList.toggle('show');
            e.stopPropagation();
        });
    });

    // Asegura que el menú completo se cierre si haces clic fuera
    document.addEventListener('click', function (e) {
        document.querySelectorAll('.dropdown-menu .show').forEach(function (dropdown) {
            dropdown.classList.remove('show');
        });
    });


    const nombreOption = document.getElementById('nombreOption');
    const usuarioOption = document.getElementById('usuarioOption');
    const selectedOptionText = document.getElementById('selectedOptionText');
    const dynamicForm = document.getElementById('dynamicForm');
    const dynamicLabel = document.getElementById('dynamicLabel');
    const dynamicInput = document.getElementById('dynamicInput');

    // Cuando se selecciona "Nombre"
    nombreOption.addEventListener('click', function(e) {
        e.preventDefault();
        selectedOptionText.innerText = 'Has seleccionado: Nombre';
        dynamicLabel.innerText = 'Nombre del Proyecto';
        dynamicInput.placeholder = 'Ingresa el nombre del proyecto';
        dynamicForm.style.display = 'block';
    });

    // Cuando se selecciona "Usuario"
    usuarioOption.addEventListener('click', function(e) {
        e.preventDefault();
        selectedOptionText.innerText = 'Has seleccionado: Usuario';
        dynamicLabel.innerText = 'Nombre del Usuario';
        dynamicInput.placeholder = 'Ingresa el nombre del usuario';
        dynamicForm.style.display = 'block';
    });