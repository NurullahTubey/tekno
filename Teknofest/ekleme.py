from PyQt5 import QtWidgets, QtWebEngineWidgets, QtCore
import ekleme_python  # UI dosyanı içe aktar
import os

class eklemePage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ekleform = ekleme_python.Ui_Form()
        self.ekleform.setupUi(self)

        # WebEngineView'in doğru ismini kullan
        self.webview = self.ekleform.EklemeHaritasi  # Güncellenmiş isim kullanıldı!

        # WebEngineView’in pencere boyutuna uyum sağlamasını sağla
        self.webview.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.webview.resize(self.width(), self.height())  # Pencere boyutuna tam uyacak

        # Eğer layout içinde değilse, yeniden ekleyelim
        if self.webview.parent() is None:
            layout = QtWidgets.QVBoxLayout(self)
            layout.addWidget(self.webview)
            self.setLayout(layout)

        # Harita dosyasının tam yolunu al ve yükle
        file_path = os.path.abspath("map.html")
        local_url = QtCore.QUrl.fromLocalFile(file_path)
        self.webview.setUrl(local_url)
