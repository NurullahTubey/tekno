import os
import json
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import QStringListModel, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

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

        # Ana sayfadaki harita için WebEngineView bileşenini al
        self.webview = self.anaform.AnaHarita  # UI dosyasındaki AnaHarita adlı QWebEngineView

        # Harita dosyasını yükle
        file_path = os.path.abspath("map.html")
        local_url = QUrl.fromLocalFile(file_path)
        self.webview.setUrl(local_url)

    def Ekle(self):
        """Ekleme butonuna basınca ekleme sayfasını açar ve ana sayfayı tamamen kapatır."""
        text = self.anaform.lineEdit_ekle.text().strip()

        if not text:
            QMessageBox.warning(self, "Hata", "Lütfen bir isim giriniz!")
            return

        # Aynı ismin daha önce eklenip eklenmediğini kontrol et
        if text in self.liste_elemanlari:
            QMessageBox.warning(self, "Hata", "Bu isim zaten eklenmiş!")
            return

        # Geçici olarak listeye ekle
        self.liste_elemanlari.append(text)
        self.model.setStringList(self.liste_elemanlari)
        self.model.layoutChanged.emit()
        self.kaydet_verileri()

        self.anaform.lineEdit_ekle.clear()

        # Ekleme penceresini aç
        self.close()
        self.ekleme_pencere_ac.show()

        # Kullanıcı pencereyi kapattığında kontrol et
        self.ekleme_pencere_ac.closeEvent = self.ekleme_kontrol

    def Sil(self):
        """ListView üzerinden seçilen veya lineEdit_sil içindeki metne göre elemanı siler."""
        selected_index = self.anaform.listView.currentIndex().row()
        silinecek_metin = self.anaform.lineEdit_sil.text().strip()

        if selected_index != -1:  # Eğer listView'den seçim yapılmışsa
            silinecek_metin = self.liste_elemanlari[selected_index]

        if silinecek_metin in self.liste_elemanlari:
            self.liste_elemanlari.remove(silinecek_metin)  # Listeden çıkar
            self.model.setStringList(self.liste_elemanlari)  # Listeyi güncelle
            self.model.layoutChanged.emit()  # Güncelleme sinyali gönder
            self.kaydet_verileri()  # JSON dosyasını güncelle

            # lineEdit_sil temizle
            self.anaform.lineEdit_sil.clear()

        else:
            QMessageBox.warning(self, "Hata", "Silinecek öğe bulunamadı!")

    def ekleme_kontrol(self, event):
        """Ekleme penceresi kapandığında iptal edilip edilmediğini kontrol eder."""
        if self.ekleme_pencere_ac.iptal_edildi:
            # Eğer iptal edildiyse, son eklenen öğeyi kaldır
            if self.liste_elemanlari:
                self.liste_elemanlari.pop()
                self.model.setStringList(self.liste_elemanlari)
                self.model.layoutChanged.emit()
                self.kaydet_verileri()
        
        # Ana sayfayı tekrar aç
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
