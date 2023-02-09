from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_Extrato(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(595, 619)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(180, 20, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(45)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(90, 90, 381, 401))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 379, 399))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.extrato = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.extrato.setGeometry(QtCore.QRect(10, 20, 311, 271))
        self.extrato.setText("")
        self.extrato.setObjectName("extrato")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(240, 510, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 560, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Extrato"))
        self.pushButton.setText(_translate("Form", "VOLTAR"))
        self.pushButton_2.setText(_translate("Form", "SAIR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Tela_Extrato()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())