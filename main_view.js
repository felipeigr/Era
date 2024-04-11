// Seleccionamos todas las imágenes con la clase "maxSize"
const imagenes = document.querySelectorAll('.maxSize');

// Añadimos un evento de "mouseenter" a cada imagen
imagenes.forEach(imagen => {
    imagen.addEventListener('mouseenter', () => {
        // Al pasar el mouse sobre una imagen, la imagen se expandirá para llenar toda la caja
        imagen.style.transform = 'scale(1.5)'; // Escalamos la imagen al 150%
    });

    // Añadimos un evento de "mouseleave" a cada imagen
    imagen.addEventListener('mouseleave', () => {
        // Al sacar el mouse de una imagen, la imagen volverá a su tamaño original
        imagen.style.transform = 'scale(1)'; // Volvemos a la escala original (100%)
    });
});