// Seleccionar el botón del menú desplegable
const dropdownButton = document.getElementById('btn-filtro');
                    
// Agregar evento de clic al botón del menú desplegable
dropdownButton.addEventListener('click', function (e) {
    const dropdownMenu = this.nextElementSibling; // Obtener el menú desplegable
    dropdownMenu.classList.toggle('show'); // Alternar la visibilidad del menú
});

// Manejar clics en el submenú
document.querySelectorAll('.dropdown-submenu > .dropdown-item').forEach(item => {
    item.addEventListener('click', function (e) {
        e.preventDefault(); // Prevenir el comportamiento predeterminado
        const submenu = this.nextElementSibling; // Obtener el submenú
        submenu.classList.toggle('show'); // Alternar visibilidad del submenú
    });
});

// Cerrar el submenú al hacer clic fuera del menú
document.addEventListener('click', function (e) {
    if (!e.target.closest('.dropdown')) {
        document.querySelectorAll('.dropdown-menu .dropdown-menu').forEach(sub => {
            sub.classList.remove('show');
        });
    }

     // Función para manejar la selección de opciones
    function selectOption(option) {
        console.log("Seleccionaste:", option); // Mostrar la opción seleccionada en la consola
        const dropdownMenu = document.querySelector('.dropdown-menu'); // Obtener el menú desplegable
        dropdownMenu.classList.remove('show'); // Cerrar el menú al seleccionar una opción
    }
});