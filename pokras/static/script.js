document.addEventListener('DOMContentLoaded', () => {
    const mapObject = document.getElementById('map');

    mapObject.addEventListener('load', () => {
        const svgDoc = mapObject.contentDocument;
        const territories = svgDoc.querySelectorAll('path');

        territories.forEach(territory => {
            territory.addEventListener('click', () => {
                territory.style.fill = 'red';
            });
        });
    });

    fetch('/game')
        .then(response => response.json())
        .then(data => console.log(data));
});
