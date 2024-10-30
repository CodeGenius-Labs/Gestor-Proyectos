 
            document.getElementById('btn-crear-usuario').addEventListener('click', function() {
                document.getElementById('modalsu').style.display = 'block';
                document.getElementById('user_id').value = this.getAttribute('data-id');
                document.getElementById('username').value = this.getAttribute('data-username');
                document.getElementById('email').value = this.getAttribute('data-email');
            });
            document.getElementById('btn-crear-usuario-side').addEventListener('click', function() {
                document.getElementById('modalsu').style.display = 'block';
                document.getElementById('user_id').value = this.getAttribute('data-id');
                document.getElementById('username').value = this.getAttribute('data-username');
                document.getElementById('email').value = this.getAttribute('data-email');
            });
            window.onclick = function(event) {
                var modal = document.getElementById('modalsu');
                if (event.target == modal) {
                    modal.style.display = 'none';
                }
            };