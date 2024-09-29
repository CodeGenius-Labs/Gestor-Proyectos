const modal4 = document.getElementById('modal4');
const closeBtn = document.querySelector('.close-btn-modal4');


function openModal4() {
    modal4.style.display = 'block';
}


function closeModal4() {
    modal4.style.display = 'none';
}
closeBtn.onclick = function () {
    closeModal4();
}

window.onclick = function (event) {
    if (event.target == modal4) {
        closeModal4();
    }
}





document.addEventListener('DOMContentLoaded', function () {
    const modal5 = document.getElementById('modal5');
    const closeBtn5 = document.querySelector('.close-btn-modal5');

    function openModal5() {
        modal5.style.display = 'block';
    }

    function closeModal5() {
        modal5.style.display = 'none';
    }


    closeBtn5.onclick = function () {
        closeModal5();
    }

    window.onclick = function (event) {
        if (event.target == modal5) {
            closeModal5();
        }
    }
});



