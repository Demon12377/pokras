document.addEventListener("DOMContentLoaded", () => {
    fetch('/static/karata.svg')
        .then(response => response.text())
        .then(svgData => {
            document.getElementById('map-container').innerHTML = svgData;
        });
});
