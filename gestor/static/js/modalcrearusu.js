 
            document.getElementById('btn-crear-usuario').addEventListener('click', function() {
                document.getElementById('modalsu').style.display = 'block';
            });

            
            document.getElementById('closeModalsuBtn').addEventListener('click', function() {
                document.getElementById('modalsu').style.display = 'none';
            });

            
            window.onclick = function(event) {
                var modal = document.getElementById('modalsu');
                if (event.target == modal) {
                    modal.style.display = 'none';
                }
            };