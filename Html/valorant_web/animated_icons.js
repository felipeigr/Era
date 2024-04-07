document.addEventListener('DOMContentLoaded', () => {
    const imagenes = document.querySelectorAll('.navbar-brand img');

    imagenes.forEach(imagen => {
        imagen.addEventListener('mouseenter', () => {
            imagen.style.transform = 'scale(1.5)'; 
            imagen.style.transition = 'transform 0.3s ease-in-out';
        });

        imagen.addEventListener('mouseleave', () => {
            imagen.style.transform = 'scale(1)'; 
        });
    });
});
