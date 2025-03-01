import os
import json
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import QStringListModel

import AnaSayfa_python
from ekleme import eklemePage

DATA_FILE = "liste_verileri.json"  # Kaydedilecek dosya

class anasayfaPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.anaform = AnaSayfa_python.Ui_MainWindow()
        self.anaform.setupUi(self)
        self.ekleme_pencere_ac = eklemePage()

        # Ekleme penceresi kapanınca ana sayfayı tekrar aç
        self.ekleme_pencere_ac.closeEvent = self.ekleme_kapaninca_ac

        # Liste için model oluştur
        self.model = QStringListModel()
        self.liste_elemanlari = self.yukle_verileri()
        self.model.setStringList(self.liste_elemanlari)
        self.anaform.listView.setModel(self.model)

        # Buton sinyalleri
        self.anaform.Buton_ekle.clicked.connect(self.Ekle)
        self.anaform.Buton_sil.clicked.connect(self.Sil)

    def Ekle(self):
        """Ekleme butonuna basınca ekleme sayfasını açar ve ana sayfayı tamamen kapatır."""
        text = self.anaform.lineEdit_ekle.text().strip()

        if not text:
            QMessageBox.warning(self, "Hata", "Lütfen bir isim giriniz!")
            return

        self.liste_elemanlari.append(text)
        self.model.setStringList(self.liste_elemanlari)
        self.model.layoutChanged.emit()
        self.kaydet_verileri()
        self.anaform.lineEdit_ekle.clear()

        # Ana sayfayı tamamen kapat ve ekleme penceresini aç
        self.close()  # Ana sayfayı tamamen kapat
        self.ekleme_pencere_ac.show()

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

    def ekleme_kapaninca_ac(self, event):
        """Ekleme penceresi kapanınca ana sayfayı tekrar açar."""
        self.__init__()  # Ana sayfa yeniden başlat
        self.show()  # Ana sayfayı tekrar göster
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
