# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(978, 803)
        MainWindow.setMinimumSize(QtCore.QSize(978, 803))
        MainWindow.setMaximumSize(QtCore.QSize(978, 803))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/icons8-guitar-strings-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("  QTabWidget::pane { /* The tab widget frame */\n"
"      border-top: 2px solid #C2C7CB;\n"
"      position: absolute;\n"
"      top: -0.5em;\n"
"  }\n"
"\n"
"  QTabWidget::tab-bar {\n"
"      alignment: center;\n"
"  }\n"
"\n"
"  /* Style the tab using the tab sub-control. Note that\n"
"      it reads QTabBar _not_ QTabWidget */\n"
"  QTabBar::tab {\n"
"      background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                  stop: 0 #E1E1E1, stop: 0.4 #DDDDDD,\n"
"                                  stop: 0.5 #D8D8D8, stop: 1.0 #D3D3D3);\n"
"      border: 2px solid #C4C4C3;\n"
"      border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"      border-top-left-radius: 4px;\n"
"      border-top-right-radius: 4px;\n"
"      min-width: 8ex;\n"
"      padding: 2px;\n"
"  }\n"
"\n"
"  QTabBar::tab:selected, QTabBar::tab:hover {\n"
"      background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                  stop: 0 #fafafa, stop: 0.4 #f4f4f4,\n"
"                                  stop: 0.5 #e7e7e7, stop: 1.0 #fafafa);\n"
"  }\n"
"\n"
"  QTabBar::tab:selected {\n"
"      border-color: #9B9B9B;\n"
"      border-bottom-color: #C2C7CB; /* same as pane color */\n"
"  }\n"
"\n"
"QWidget#tab{\n"
"background-image: url(/home/ahmad/PycharmProjects/Musical-Instruments-Simulation/icons/guitar.jpg); \n"
"background-position: center;\n"
"background-size : auto;\n"
" }\n"
"QWidget#tab_2{\n"
"background-image: url(/home/ahmad/PycharmProjects/Musical-Instruments-Simulation/icons/piano.jpg); \n"
"background-position: center ;\n"
"background-repeat: no-repeat;\n"
"background-size : cover;\n"
" }")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_3.addLayout(self.verticalLayout_5)
        spacerItem = QtWidgets.QSpacerItem(20, 250, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_3.addItem(spacerItem)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.guitar_e = QtWidgets.QPushButton(self.tab)
        self.guitar_e.setText("")
        self.guitar_e.setFlat(True)
        self.guitar_e.setProperty("key_number", 20)
        self.guitar_e.setObjectName("guitar_e")
        self.verticalLayout_4.addWidget(self.guitar_e)
        spacerItem1 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_4.addItem(spacerItem1)
        self.guitar_a = QtWidgets.QPushButton(self.tab)
        self.guitar_a.setText("")
        self.guitar_a.setFlat(True)
        self.guitar_a.setProperty("key_number", 24)
        self.guitar_a.setObjectName("guitar_a")
        self.verticalLayout_4.addWidget(self.guitar_a)
        spacerItem2 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_4.addItem(spacerItem2)
        self.guitar_d = QtWidgets.QPushButton(self.tab)
        self.guitar_d.setText("")
        self.guitar_d.setFlat(True)
        self.guitar_d.setProperty("key_number", 28)
        self.guitar_d.setObjectName("guitar_d")
        self.verticalLayout_4.addWidget(self.guitar_d)
        spacerItem3 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_4.addItem(spacerItem3)
        self.guitar_g = QtWidgets.QPushButton(self.tab)
        self.guitar_g.setText("")
        self.guitar_g.setFlat(True)
        self.guitar_g.setProperty("key_number", 32)
        self.guitar_g.setObjectName("guitar_g")
        self.verticalLayout_4.addWidget(self.guitar_g)
        spacerItem4 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_4.addItem(spacerItem4)
        self.guitar_b = QtWidgets.QPushButton(self.tab)
        self.guitar_b.setText("")
        self.guitar_b.setFlat(True)
        self.guitar_b.setProperty("key_number", 36)
        self.guitar_b.setObjectName("guitar_b")
        self.verticalLayout_4.addWidget(self.guitar_b)
        spacerItem5 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_4.addItem(spacerItem5)
        self.guitar_e2 = QtWidgets.QPushButton(self.tab)
        self.guitar_e2.setText("")
        self.guitar_e2.setFlat(True)
        self.guitar_e2.setProperty("key_number", 40)
        self.guitar_e2.setObjectName("guitar_e2")
        self.verticalLayout_4.addWidget(self.guitar_e2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_4.addItem(spacerItem6)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem7 = QtWidgets.QSpacerItem(20, 250, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_6.addItem(spacerItem7)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem8)
        self.verticalLayout_3.addLayout(self.verticalLayout_6)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/icons8-guitar-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab, icon1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.piano_1 = QtWidgets.QPushButton(self.tab_2)
        self.piano_1.setGeometry(QtCore.QRect(0, 50, 71, 661))
        self.piano_1.setText("")
        self.piano_1.setFlat(True)
        self.piano_1.setProperty("key_number", 28)
        self.piano_1.setObjectName("piano_1")
        self.piano_2 = QtWidgets.QPushButton(self.tab_2)
        self.piano_2.setGeometry(QtCore.QRect(40, 50, 71, 421))
        self.piano_2.setText("")
        self.piano_2.setFlat(True)
        self.piano_2.setProperty("key_number", 29)
        self.piano_2.setObjectName("piano_2")
        self.piano_3 = QtWidgets.QPushButton(self.tab_2)
        self.piano_3.setGeometry(QtCore.QRect(90, 50, 71, 661))
        self.piano_3.setText("")
        self.piano_3.setFlat(True)
        self.piano_3.setProperty("key_number", 30)
        self.piano_3.setObjectName("piano_3")
        self.piano_5 = QtWidgets.QPushButton(self.tab_2)
        self.piano_5.setGeometry(QtCore.QRect(200, 50, 71, 661))
        self.piano_5.setText("")
        self.piano_5.setFlat(True)
        self.piano_5.setProperty("key_number", 32)
        self.piano_5.setObjectName("piano_5")
        self.piano_4 = QtWidgets.QPushButton(self.tab_2)
        self.piano_4.setGeometry(QtCore.QRect(150, 50, 71, 421))
        self.piano_4.setText("")
        self.piano_4.setFlat(True)
        self.piano_4.setProperty("key_number", 31)
        self.piano_4.setObjectName("piano_4")
        self.piano_6 = QtWidgets.QPushButton(self.tab_2)
        self.piano_6.setGeometry(QtCore.QRect(270, 50, 71, 661))
        self.piano_6.setText("")
        self.piano_6.setFlat(True)
        self.piano_6.setProperty("key_number", 33)
        self.piano_6.setObjectName("piano_6")
        self.piano_8 = QtWidgets.QPushButton(self.tab_2)
        self.piano_8.setGeometry(QtCore.QRect(380, 50, 71, 661))
        self.piano_8.setText("")
        self.piano_8.setFlat(True)
        self.piano_8.setProperty("key_number", 35)
        self.piano_8.setObjectName("piano_8")
        self.piano_10 = QtWidgets.QPushButton(self.tab_2)
        self.piano_10.setGeometry(QtCore.QRect(490, 50, 71, 661))
        self.piano_10.setText("")
        self.piano_10.setFlat(True)
        self.piano_10.setProperty("key_number", 37)
        self.piano_10.setObjectName("piano_10")
        self.piano_12 = QtWidgets.QPushButton(self.tab_2)
        self.piano_12.setGeometry(QtCore.QRect(580, 50, 71, 661))
        self.piano_12.setText("")
        self.piano_12.setFlat(True)
        self.piano_12.setProperty("key_number", 39)
        self.piano_12.setObjectName("piano_12")
        self.piano_13 = QtWidgets.QPushButton(self.tab_2)
        self.piano_13.setGeometry(QtCore.QRect(680, 40, 71, 661))
        self.piano_13.setText("")
        self.piano_13.setFlat(True)
        self.piano_13.setProperty("key_number", 40)
        self.piano_13.setObjectName("piano_13")
        self.piano_15 = QtWidgets.QPushButton(self.tab_2)
        self.piano_15.setGeometry(QtCore.QRect(780, 50, 71, 661))
        self.piano_15.setText("")
        self.piano_15.setFlat(True)
        self.piano_15.setProperty("key_number", 42)
        self.piano_15.setObjectName("piano_15")
        self.piano_17 = QtWidgets.QPushButton(self.tab_2)
        self.piano_17.setGeometry(QtCore.QRect(880, 50, 71, 661))
        self.piano_17.setText("")
        self.piano_17.setFlat(True)
        self.piano_17.setProperty("key_number", 44)
        self.piano_17.setObjectName("piano_17")
        self.piano_16 = QtWidgets.QPushButton(self.tab_2)
        self.piano_16.setGeometry(QtCore.QRect(840, 50, 71, 421))
        self.piano_16.setText("")
        self.piano_16.setFlat(True)
        self.piano_16.setProperty("key_number", 43)
        self.piano_16.setObjectName("piano_16")
        self.piano_14 = QtWidgets.QPushButton(self.tab_2)
        self.piano_14.setGeometry(QtCore.QRect(710, 40, 71, 421))
        self.piano_14.setText("")
        self.piano_14.setFlat(True)
        self.piano_14.setProperty("key_number", 41)
        self.piano_14.setObjectName("piano_14")
        self.piano_11 = QtWidgets.QPushButton(self.tab_2)
        self.piano_11.setGeometry(QtCore.QRect(540, 50, 71, 421))
        self.piano_11.setText("")
        self.piano_11.setFlat(True)
        self.piano_11.setProperty("key_number", 38)
        self.piano_11.setObjectName("piano_11")
        self.piano_9 = QtWidgets.QPushButton(self.tab_2)
        self.piano_9.setGeometry(QtCore.QRect(430, 50, 71, 421))
        self.piano_9.setText("")
        self.piano_9.setFlat(True)
        self.piano_9.setProperty("key_number", 36)
        self.piano_9.setObjectName("piano_9")
        self.piano_7 = QtWidgets.QPushButton(self.tab_2)
        self.piano_7.setGeometry(QtCore.QRect(330, 50, 71, 421))
        self.piano_7.setText("")
        self.piano_7.setFlat(True)
        self.piano_7.setProperty("key_number", 34)
        self.piano_7.setObjectName("piano_7")
        self.piano_17.raise_()
        self.piano_1.raise_()
        self.piano_3.raise_()
        self.piano_2.raise_()
        self.piano_5.raise_()
        self.piano_4.raise_()
        self.piano_6.raise_()
        self.piano_8.raise_()
        self.piano_10.raise_()
        self.piano_12.raise_()
        self.piano_13.raise_()
        self.piano_15.raise_()
        self.piano_16.raise_()
        self.piano_11.raise_()
        self.piano_9.raise_()
        self.piano_7.raise_()
        self.piano_14.raise_()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/icons8-piano-96.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon2, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 978, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Synthetic Instruments"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Guitar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Piano"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

