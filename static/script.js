document.addEventListener("DOMContentLoaded", () => {
    fetch('/static/karata.svg')
        .then(response => response.text())
        .then(svgData => {
            document.getElementById('map-container').innerHTML = svgData;
        });

    const form = document.getElementById('colorize-form');
    form.addEventListener('submit', (event) => {
        event.preventDefault();
        const territoryId = event.target.elements.territory.value;
        const color = event.target.elements.color.value;
        const territoryElement = document.getElementById(territoryId);
        if (territoryElement) {
            territoryElement.setAttribute('fill', color);
        }
    });
});
