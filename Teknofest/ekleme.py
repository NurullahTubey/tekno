from PyQt5 import QtWidgets, QtWebEngineWidgets, QtCore
import ekleme_python  # UI dosyanı içe aktar
import os

class eklemePage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ekleform = ekleme_python.Ui_Form()
        self.ekleform.setupUi(self)
        self.webview = self.ekleform.EklemeHaritasi

        self.webview.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.webview.resize(self.width(), self.height())

        if self.webview.parent() is None:
            layout = QtWidgets.QVBoxLayout(self)
            layout.addWidget(self.webview)
            self.setLayout(layout)

        file_path = os.path.abspath("map.html")
        local_url = QtCore.QUrl.fromLocalFile(file_path)
        self.webview.setUrl(local_url)

        # İptal butonuna tıklanınca pencereyi kapat
        self.ekleform.pushButton_2.clicked.connect(self.close)
