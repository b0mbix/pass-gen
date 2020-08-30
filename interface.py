from PyQt5 import QtCore, QtGui, QtWidgets
from generator import generating_pass

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        #Main window
        MainWindow.setObjectName("MainWindow")
        MainWindow.setGeometry(200, 200, 800, 600)
        font = QtGui.QFont()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        #Title and welcome
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(300, 30, 200, 50))
        font.setFamily("Lato")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.title.setFont(font)
        self.title.setObjectName("title")

        self.text1 = QtWidgets.QLabel(self.centralwidget)
        self.text1.setGeometry(QtCore.QRect(70, 110, 270, 30))
        font.setPointSize(16)
        self.text1.setFont(font)
        self.text1.setObjectName("text1")


        #Lenght widgets
        self.text2 = QtWidgets.QLabel(self.centralwidget)
        self.text2.setGeometry(QtCore.QRect(70, 165, 281, 20))
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.text2.setFont(font)
        self.text2.setObjectName("text2")

        self.inputLenght = QtWidgets.QSpinBox(self.centralwidget)
        self.inputLenght.setGeometry(QtCore.QRect(360, 160, 60, 30))
        self.inputLenght.setFont(font)
        self.inputLenght.setMinimum(1)
        self.inputLenght.setMaximum(256)
        self.inputLenght.setProperty("value", 16)
        self.inputLenght.setObjectName("inputLenght")


        #Checkbox widgets
        self.text3 = QtWidgets.QLabel(self.centralwidget)
        self.text3.setGeometry(QtCore.QRect(70, 200, 200, 25))
        self.text3.setFont(font)
        self.text3.setObjectName("text3")

        self.checkboxLower = QtWidgets.QCheckBox(self.centralwidget)
        self.checkboxLower.setGeometry(QtCore.QRect(100, 235, 200, 25))
        self.checkboxLower.setFont(font)
        self.checkboxLower.setObjectName("checkboxLower")

        self.checkboxUpper = QtWidgets.QCheckBox(self.centralwidget)
        self.checkboxUpper.setGeometry(QtCore.QRect(100, 270, 200, 25))
        self.checkboxUpper.setFont(font)
        self.checkboxUpper.setObjectName("checkboxUpper")

        self.checkboxNumber = QtWidgets.QCheckBox(self.centralwidget)
        self.checkboxNumber.setGeometry(QtCore.QRect(100, 305, 200, 25))
        self.checkboxNumber.setFont(font)
        self.checkboxNumber.setObjectName("checkboxNumber")

        self.checkboxSymbol = QtWidgets.QCheckBox(self.centralwidget)
        self.checkboxSymbol.setGeometry(QtCore.QRect(100, 340, 200, 25))
        self.checkboxSymbol.setFont(font)
        self.checkboxSymbol.setObjectName("checkboxSymbol")


        #Generate button
        self.buttonGenerate = QtWidgets.QPushButton(self.centralwidget)
        self.buttonGenerate.setGeometry(QtCore.QRect(110, 380, 90, 25))
        font.setPointSize(11)
        self.buttonGenerate.setFont(font)
        self.buttonGenerate.setObjectName("buttonGenerate")


        #Generated password
        self.linePassword = QtWidgets.QLineEdit(self.centralwidget)
        self.linePassword.setGeometry(QtCore.QRect(70, 440, 550, 25))
        self.linePassword.setFont(font)
        self.linePassword.setFrame(True)
        self.linePassword.setReadOnly(False)
        self.linePassword.setObjectName("linePassword")

        self.buttonCopy = QtWidgets.QPushButton(self.centralwidget)
        self.buttonCopy.setGeometry(QtCore.QRect(640, 440, 75, 25))
        self.buttonCopy.setFont(font)
        self.buttonCopy.setObjectName("buttonCopy")


        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.buttonGenerate.clicked.connect(self.generating)
        self.buttonCopy.clicked.connect(self.copying)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PassGen"))
        self.title.setText(_translate("MainWindow", "PassGen"))
        self.text1.setText(_translate("MainWindow", "Let\'s create your password!"))
        self.text2.setText(_translate("MainWindow", "Enter your password lenght (max 256):"))
        self.text3.setText(_translate("MainWindow", "What should be in it?"))
        self.checkboxLower.setText(_translate("MainWindow", "Lowercase characters"))
        self.checkboxUpper.setText(_translate("MainWindow", "Uppercase characters"))
        self.checkboxNumber.setText(_translate("MainWindow", "Numbers"))
        self.checkboxSymbol.setText(_translate("MainWindow", "Symbols"))
        self.buttonGenerate.setText(_translate("MainWindow", "Generate!"))
        self.buttonCopy.setText(_translate("MainWindow", "Copy"))

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
            msgErr.setWindowTitle("Invalid data!")
            msgErr.setText("Please give correct data!")
            msgErr.setIcon(QtWidgets.QMessageBox.Critical)
            msgErr.exec_()

    def copying(self):
        clipboard = QtWidgets.QApplication.clipboard()
        clipboard.setText(self.linePassword.displayText())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    QtGui.QFontDatabase.addApplicationFont("fonts/Roboto-Regular.ttf")
    QtGui.QFontDatabase.addApplicationFont("fonts/Lato-Regular.ttf")
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
