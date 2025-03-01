from PyQt5 import QtWidgets
import ekleme_python  # UI dosyanı içe aktar

class eklemePage(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ekleform = ekleme_python.Ui_Form()
        self.ekleform.setupUi(self)
