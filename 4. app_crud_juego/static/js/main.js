// Selección de elementos
const themeToggle = document.getElementById('theme-toggle');
const body = document.body;

// Función para alternar tema
themeToggle.addEventListener('click', () => {
    body.classList.toggle('light');
    if (body.classList.contains('light')) {
        themeToggle.textContent = 'Cambiar a Dark';
    } else {
        themeToggle.textContent = 'Cambiar a Light';
    }
});
