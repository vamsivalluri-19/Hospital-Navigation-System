document.addEventListener('DOMContentLoaded', function() {
    const map = L.map('map').setView([28.6139, 77.2090], 13); // Example coordinates for New Delhi

    // Add OpenStreetMap tiles
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    // Add a marker to the map
    L.marker([28.6139, 77.2090]).addTo(map)
        .bindPopup('Hospital Location')
        .openPopup();
});
