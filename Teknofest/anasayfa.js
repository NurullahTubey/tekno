
var map = L.map('map').setView([39.41926314234217, 29.985403641671002], 17);

// OpenStreetMap katmanı ekle
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap Katkıda Bulunanlar'
}).addTo(map);

// Test amaçlı bir marker ekleyelim
L.marker([39.41926314234217, 29.985403641671002]).addTo(map)
    .bindPopup('Merkez İstasyon')
    .openPopup();
// Drone bilgilerini göstereceğimiz alanı seç
const droneBar = document.querySelector(".dronebar ul");

// Drone verilerini güncelleyen fonksiyon
function updateDroneInfo(data) {
    droneBar.innerHTML = `
        <li><strong>Hız:</strong> ${data.hiz} km/h</li>
        <li><strong>Yükseklik:</strong> ${data.yukseklik} m</li>
        <li><strong>Şarj:</strong> ${data.sarj}%</li>
        <li><strong>Merkez Uzaklık:</strong> ${data.mesafe} m</li>
    `;
}

// Gerçek zamanlı veri simülasyonu (WebSocket veya API çağrısı yerine)
function fetchDroneData() {
    const droneData = {
        hiz: Math.floor(Math.random() * 50), // 0-50 km/h arasında rastgele hız
        yukseklik: Math.floor(Math.random() * 200), // 0-200 m arasında rastgele yükseklik
        sarj: Math.floor(Math.random() * 100), // 0-100% arasında rastgele şarj
        mesafe: Math.floor(Math.random() * 500) // 0-500 m arasında rastgele mesafe
    };

    updateDroneInfo(droneData);
}

// Her 2 saniyede bir yeni drone verisini simüle et
setInterval(fetchDroneData, 2000);

// Sayfa yüklendiğinde ilk değerleri göster
fetchDroneData();
