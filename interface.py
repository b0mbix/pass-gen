from PyQt5 import QtCore, QtGui, QtWidgets
from generator import generating_pass

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #Main window
        icon = QtGui.QIcon()
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(200, 200, 800, 600)
        MainWindow.setWindowTitle("PassGen")
        MainWindow.setWindowIcon(QtGui.QIcon('img/logo.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        #Title and welcome
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(300, 30, 200, 50))
        font.setFamily("Lato")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.title.setFont(font)

        self.text1 = QtWidgets.QLabel(self.centralwidget)
        self.text1.setGeometry(QtCore.QRect(70, 110, 270, 30))
        font.setPointSize(16)
        self.text1.setFont(font)


        #Lenght widgets
        self.text2 = QtWidgets.QLabel(self.centralwidget)
        self.text2.setGeometry(QtCore.QRect(70, 165, 290, 20))
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.text2.setFont(font)

        self.inputLenght = QtWidgets.QSpinBox(self.centralwidget)
        self.inputLenght.setGeometry(QtCore.QRect(360, 160, 60, 30))
        self.inputLenght.setFont(font)
        self.inputLenght.setMinimum(1)
        self.inputLenght.setMaximum(256)
        self.inputLenght.setProperty("value", 16)


        #Checkbox widgets
        self.text3 = QtWidgets.QLabel(self.centralwidget)
        self.text3.setGeometry(QtCore.QRect(70, 200, 200, 25))
        self.text3.setFont(font)

        self.checkboxLower = QtWidgets.QCheckBox(self.centralwidget)
        self.checkboxLower.setGeometry(QtCore.QRect(100, 235, 200, 25))
        self.checkboxLower.setFont(font)

        self.checkboxUpper = QtWidgets.QCheckBox(self.centralwidget)
        self.checkboxUpper.setGeometry(QtCore.QRect(100, 270, 200, 25))
        self.checkboxUpper.setFont(font)

        self.checkboxNumber = QtWidgets.QCheckBox(self.centralwidget)
        self.checkboxNumber.setGeometry(QtCore.QRect(100, 305, 200, 25))
        self.checkboxNumber.setFont(font)

        self.checkboxSymbol = QtWidgets.QCheckBox(self.centralwidget)
        self.checkboxSymbol.setGeometry(QtCore.QRect(100, 340, 200, 25))
        self.checkboxSymbol.setFont(font)


        #Generate button
        self.buttonGenerate = QtWidgets.QPushButton(self.centralwidget)
        self.buttonGenerate.setGeometry(QtCore.QRect(110, 380, 90, 25))
        font.setPointSize(11)
        self.buttonGenerate.setFont(font)


        #Generated password
        self.linePassword = QtWidgets.QLineEdit(self.centralwidget)
        self.linePassword.setGeometry(QtCore.QRect(70, 440, 550, 25))
        self.linePassword.setFont(font)
        self.linePassword.setFrame(True)
        self.linePassword.setReadOnly(False)

        self.buttonCopy = QtWidgets.QPushButton(self.centralwidget)
        self.buttonCopy.setGeometry(QtCore.QRect(640, 440, 75, 25))
        self.buttonCopy.setFont(font)


        #Language change
        self.english = QtWidgets.QPushButton(self.centralwidget)
        self.english.setGeometry(QtCore.QRect(590, 525, 80, 40))
        icon.addPixmap(QtGui.QPixmap("img/english.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.english.setIcon(icon)
        self.english.setIconSize(QtCore.QSize(80, 40))

        self.polish = QtWidgets.QPushButton(self.centralwidget)
        self.polish.setGeometry(QtCore.QRect(690, 525, 80, 40))
        icon.addPixmap(QtGui.QPixmap("img/polish.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.polish.setIcon(icon)
        self.polish.setIconSize(QtCore.QSize(80, 40))


        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow, "en")
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.buttonGenerate.clicked.connect(self.generating)
        self.buttonCopy.clicked.connect(self.copying)
        self.english.clicked.connect(lambda: self.retranslateUi(MainWindow, "en"))
        self.polish.clicked.connect(lambda: self.retranslateUi(MainWindow, "pl"))

    def retranslateUi(self, MainWindow, lang):
        _translate = QtCore.QCoreApplication.translate
        self.title.setText(_translate("MainWindow", "PassGen"))
        self.text1.setText(_translate("MainWindow", "Let\'s create your password!" if lang == "en" else "Stwórz swoje hasło!"))
        self.text2.setText(_translate("MainWindow", "Enter your password lenght (max 256):" if lang == "en" else "Wpisz długość swojego hasła (max 256):"))
        self.text3.setText(_translate("MainWindow", "What should be in it?" if lang == "en" else "Co ma w nim być?"))
        self.checkboxLower.setText(_translate("MainWindow", "Lowercase characters" if lang == "en" else "Małe litery"))
        self.checkboxUpper.setText(_translate("MainWindow", "Uppercase characters" if lang == "en" else "Duże litery"))
        self.checkboxNumber.setText(_translate("MainWindow", "Numbers" if lang == "en" else "Liczby"))
        self.checkboxSymbol.setText(_translate("MainWindow", "Symbols" if lang == "en" else "Symbole"))
        self.buttonGenerate.setText(_translate("MainWindow", "Generate!" if lang == "en" else "Wygeneruj!"))
        self.buttonCopy.setText(_translate("MainWindow", "Copy" if lang == "en" else "Skopiuj"))

        if lang == "en":
            self.inputLenght.setGeometry(QtCore.QRect(360, 160, 60, 30))
        else:
            self.inputLenght.setGeometry(QtCore.QRect(370, 160, 60, 30))
        self.lang = lang

    def generating(self):
        details = []

        details.append('y' if self.checkboxLower.isChecked() else 'n')
        details.append('y' if self.checkboxUpper.isChecked() else 'n')
        details.append('y' if self.checkboxNumber.isChecked() else 'n')
        details.append('y' if self.checkboxSymbol.isChecked() else 'n')

        try:
            self.linePassword.setText(generating_pass(self.inputLenght.value(), details))
        except ValueError:
            #show error pop-up
            msgErr = QtWidgets.QMessageBox()
            msgErr.setWindowTitle("Invalid data!" if self.lang == "en" else "Nieprawidłowe dane!")
            msgErr.setText("Please give correct data!" if self.lang == "en" else "Podaj prawidłowe dane!")
            msgErr.setIcon(QtWidgets.QMessageBox.Critical)
            msgErr.exec_()

    def copying(self):
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(self.linePassword.displayText())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    font = QtGui.QFont()
    QtGui.QFontDatabase.addApplicationFont("fonts/Roboto-Regular.ttf")
    QtGui.QFontDatabase.addApplicationFont("fonts/Lato-Regular.ttf")
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
