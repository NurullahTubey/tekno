import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from AnaSayfa import anasayfaPage
from ekleme import eklemePage

app = QApplication(sys.argv)
window = anasayfaPage()  # Ana sayfa penceresini başlat
window.show()  # Ana sayfayı göster
sys.exit(app.exec_())  # Uygulamayı başlat
