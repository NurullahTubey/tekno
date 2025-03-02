# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AnaSayfa.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(824, 343)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(100, 300))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_2.setSpacing(18)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.webEngineView.sizePolicy().hasHeightForWidth())
        self.webEngineView.setSizePolicy(sizePolicy)
        self.webEngineView.setMinimumSize(QtCore.QSize(0, 0))
        self.webEngineView.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView.setObjectName("webEngineView")
        self.verticalLayout_2.addWidget(self.webEngineView)
        self.AnaHarita = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AnaHarita.sizePolicy().hasHeightForWidth())
        self.AnaHarita.setSizePolicy(sizePolicy)
        self.AnaHarita.setMinimumSize(QtCore.QSize(0, 0))
        self.AnaHarita.setUrl(QtCore.QUrl("about:blank"))
        self.AnaHarita.setObjectName("AnaHarita")
        self.verticalLayout_2.addWidget(self.AnaHarita)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_sil = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_sil.sizePolicy().hasHeightForWidth())
        self.lineEdit_sil.setSizePolicy(sizePolicy)
        self.lineEdit_sil.setObjectName("lineEdit_sil")
        self.gridLayout.addWidget(self.lineEdit_sil, 2, 3, 1, 1)
        self.Buton_ekle = QtWidgets.QPushButton(self.centralwidget)
        self.Buton_ekle.setBaseSize(QtCore.QSize(0, 0))
        self.Buton_ekle.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Buton_ekle.setIconSize(QtCore.QSize(16, 16))
        self.Buton_ekle.setObjectName("Buton_ekle")
        self.gridLayout.addWidget(self.Buton_ekle, 1, 0, 1, 1)
        self.lineEdit_ekle = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_ekle.sizePolicy().hasHeightForWidth())
        self.lineEdit_ekle.setSizePolicy(sizePolicy)
        self.lineEdit_ekle.setObjectName("lineEdit_ekle")
        self.gridLayout.addWidget(self.lineEdit_ekle, 1, 3, 1, 1)
        self.Buton_sil = QtWidgets.QPushButton(self.centralwidget)
        self.Buton_sil.setBaseSize(QtCore.QSize(0, 0))
        self.Buton_sil.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Buton_sil.setIconSize(QtCore.QSize(16, 16))
        self.Buton_sil.setObjectName("Buton_sil")
        self.gridLayout.addWidget(self.Buton_sil, 2, 0, 1, 1)
        self.Buton_ayrintilar = QtWidgets.QPushButton(self.centralwidget)
        self.Buton_ayrintilar.setBaseSize(QtCore.QSize(0, 0))
        self.Buton_ayrintilar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Buton_ayrintilar.setIconSize(QtCore.QSize(16, 16))
        self.Buton_ayrintilar.setObjectName("Buton_ayrintilar")
        self.gridLayout.addWidget(self.Buton_ayrintilar, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 1)
        self.lineEdit_ayrintilar = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_ayrintilar.sizePolicy().hasHeightForWidth())
        self.lineEdit_ayrintilar.setSizePolicy(sizePolicy)
        self.lineEdit_ayrintilar.setObjectName("lineEdit_ayrintilar")
        self.gridLayout.addWidget(self.lineEdit_ayrintilar, 3, 3, 1, 1)
        self.Buton_firebase = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Buton_firebase.sizePolicy().hasHeightForWidth())
        self.Buton_firebase.setSizePolicy(sizePolicy)
        self.Buton_firebase.setObjectName("Buton_firebase")
        self.gridLayout.addWidget(self.Buton_firebase, 4, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(9, 9, 0, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setMaximumSize(QtCore.QSize(400, 16777215))
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 824, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Buton_ekle.setText(_translate("MainWindow", "Ekle"))
        self.Buton_sil.setText(_translate("MainWindow", "Sil"))
        self.Buton_ayrintilar.setText(_translate("MainWindow", "Ayrıntılar"))
        self.Buton_firebase.setText(_translate("MainWindow", "FireBase"))
        self.label.setText(_translate("MainWindow", "Toplanma Noktaları"))
from PyQt5 import QtWebEngineWidgets


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
