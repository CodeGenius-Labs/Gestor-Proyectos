
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
    
    document.addEventListener('click', function (e) {
        document.querySelectorAll('.dropdown-menu .show').forEach(function (dropdown) {
            dropdown.classList.remove('show');
        });
    });