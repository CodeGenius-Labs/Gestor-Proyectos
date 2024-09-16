document.addEventListener('DOMContentLoaded', () => {
    const botonaceptarcookies = document.getElementById('btn-aceptar-cookies');
    const avisocookies = document.getElementById('avisocookies');
    const fondoavisocookies = document.getElementById('fondoavisocookies');

    if(!localStorage.getItem('cookiesaceptadas')){
        avisocookies.classList.add('activo');
        fondoavisocookies.classList.add('activo');
    }
    

    
    botonaceptarcookies.addEventListener('click', () => {
        fondoavisocookies.classList.remove('activo');
        avisocookies.classList.remove('activo');

        localStorage.setItem('cookiesaceptadas',true);
        
    });
});



