import os
import json
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QVBoxLayout
from PyQt5.QtCore import QStringListModel, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtMultimedia import QCamera, QCameraInfo
from PyQt5.QtMultimediaWidgets import QCameraViewfinder

import AnaSayfa_python
from ekleme import eklemePage

DATA_FILE = "liste_verileri.json"  # Kaydedilecek dosya

class anasayfaPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.anaform = AnaSayfa_python.Ui_MainWindow()
        self.anaform.setupUi(self)
        self.ekleme_pencere_ac = eklemePage()

        # Liste için model oluştur
        self.model = QStringListModel()
        self.liste_elemanlari = self.yukle_verileri()
        self.model.setStringList(self.liste_elemanlari)
        self.anaform.listView.setModel(self.model)

        # Buton sinyalleri
        self.anaform.Buton_ekle.clicked.connect(self.Ekle)
        self.anaform.Buton_sil.clicked.connect(self.Sil)

        # 📌 Harita Görüntüleme
        self.webview = self.anaform.AnaHarita
        file_path = os.path.abspath("map.html")
        local_url = QUrl.fromLocalFile(file_path)
        self.webview.setUrl(local_url)

        # 📌 Kamera Görüntüsünü **tam ekran kaplayacak şekilde** ayarla
        self.kamera_aygiti = self._kamera_sec()
        if self.kamera_aygiti:
            self.kamera = QCamera(self.kamera_aygiti)
            
            # Kamera görüntüsünü tam kaplayacak şekilde ayarlayalım
            self.viewfinder = QCameraViewfinder()
            self.viewfinder.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)  
            self.viewfinder.setMinimumSize(self.anaform.kamera.size())  # Kamera alanının boyutunu al
            
            

            # Layout oluştur ve kamera alanına ekle
            layout = QVBoxLayout()
            layout.addWidget(self.viewfinder)
            layout.setContentsMargins(0, 0, 0, 0)  # Kenar boşluklarını sıfırla
            self.anaform.kamera.setLayout(layout)  

            self.kamera.setViewfinder(self.viewfinder)
            self.kamera.start()  # Kamerayı başlat

    def _kamera_sec(self):
        """Varsayılan kamerayı seçer."""
        kamera_listesi = QCameraInfo.availableCameras()
        if kamera_listesi:
            return kamera_listesi[0]  # İlk kamerayı kullan
        return None

    def Ekle(self):
        """Ekleme butonuna basınca ekleme sayfasını açar ve ana sayfayı tamamen kapatır."""
        text = self.anaform.lineEdit_ekle.text().strip()

        if not text:
            QMessageBox.warning(self, "Hata", "Lütfen bir isim giriniz!")
            return

        if text in self.liste_elemanlari:
            QMessageBox.warning(self, "Hata", "Bu isim zaten eklenmiş!")
            return

        self.liste_elemanlari.append(text)
        self.model.setStringList(self.liste_elemanlari)
        self.model.layoutChanged.emit()
        self.kaydet_verileri()

        self.anaform.lineEdit_ekle.clear()
        self.close()
        self.ekleme_pencere_ac.show()

        self.ekleme_pencere_ac.closeEvent = self.ekleme_kontrol

    def Sil(self):
        """ListView üzerinden seçilen veya lineEdit_sil içindeki metne göre elemanı siler."""
        selected_index = self.anaform.listView.currentIndex().row()
        silinecek_metin = self.anaform.lineEdit_sil.text().strip()

        if selected_index != -1:
            silinecek_metin = self.liste_elemanlari[selected_index]

        if silinecek_metin in self.liste_elemanlari:
            self.liste_elemanlari.remove(silinecek_metin)
            self.model.setStringList(self.liste_elemanlari)
            self.model.layoutChanged.emit()
            self.kaydet_verileri()

            self.anaform.lineEdit_sil.clear()
        else:
            QMessageBox.warning(self, "Hata", "Silinecek öğe bulunamadı!")

    def ekleme_kontrol(self, event):
        """Ekleme penceresi kapandığında iptal edilip edilmediğini kontrol eder."""
        if self.ekleme_pencere_ac.iptal_edildi:
            if self.liste_elemanlari:
                self.liste_elemanlari.pop()
                self.model.setStringList(self.liste_elemanlari)
                self.model.layoutChanged.emit()
                self.kaydet_verileri()
        
        self.show()
        event.accept()

    def kaydet_verileri(self):
        """Liste verilerini dosyaya kaydeder."""
        with open(DATA_FILE, "w", encoding="utf-8") as dosya:
            json.dump(self.liste_elemanlari, dosya)

    def yukle_verileri(self):
        """Kayıtlı verileri dosyadan yükler."""
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r", encoding="utf-8") as dosya:
                return json.load(dosya)
        return []
