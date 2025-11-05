document.addEventListener('DOMContentLoaded', () => {
    const mapContainer = document.getElementById('map');

    function colorMap() {
        fetch('/game')
            .then(response => response.json())
            .then(data => {
                const territories = mapContainer.querySelectorAll('path');
                territories.forEach(territory => {
                    const territoryId = territory.id;
                    if (data.territories[territoryId]) {
                        territory.setAttribute('fill', data.territories[territoryId]);
                    }
                });
            });
    }

    fetch('/static/karata.svg')
        .then(response => response.text())
        .then(svgData => {
            mapContainer.innerHTML = svgData;
            colorMap();
        });

    document.getElementById('create-country-form').addEventListener('submit', function(event) {
        event.preventDefault();

        const name = document.getElementById('name').value;
        const color = document.getElementById('color').value;
        const territory = document.getElementById('territory').value;

        fetch('/countries', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ name, color, territory }),
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            colorMap();
        });
    });
});
