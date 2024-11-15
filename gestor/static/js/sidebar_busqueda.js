function applyFilter(order, direction) {
    // Obtener la URL actual
    const url = new URL(window.location.href);
    
    // Establecer los parámetros de filtro
    url.searchParams.set('order', order);
    url.searchParams.set('direction', direction);
    
    // Redirigir a la nueva URL
    window.location.href = url.toString();
}





// Script para abrir el sidebar
const btnHamburguesa = document.getElementById('btn-hamburguesa');
const sidebar = new bootstrap.Offcanvas(document.getElementById('sidebar'));

btnHamburguesa.addEventListener('click', () => {
    sidebar.show(); // Muestra el sidebar
});
