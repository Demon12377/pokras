document.addEventListener("DOMContentLoaded", () => {
    fetch('/static/karata.svg')
        .then(response => response.text())
        .then(svgData => {
            document.getElementById('map-container').innerHTML = svgData;
            fetch('/game')
                .then(response => response.json())
                .then(data => {
                    const territories = data.territories;
                    for (const territoryId in territories) {
                        const path = document.getElementById(territoryId);
                        if (path) {
                            path.setAttribute('fill', territories[territoryId]);
                        }
                    }
                });
        });

    document.getElementById('country-form').addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(this);
        const data = Object.fromEntries(formData.entries());

        fetch('/countries', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        }).then(() => {
            // refresh map
             fetch('/game')
                .then(response => response.json())
                .then(data => {
                    const territories = data.territories;
                    for (const territoryId in territories) {
                        const path = document.getElementById(territoryId);
                        if (path) {
                            path.setAttribute('fill', territories[territoryId]);
                        }
                    }
                });
        })
    });
});
