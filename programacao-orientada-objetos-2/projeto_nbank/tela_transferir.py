from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_Transferir(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(596, 590)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(120, 60, 321, 101))
        font = QtGui.QFont()
        font.setPointSize(46)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(6, 200, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 260, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(230, 190, 261, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 250, 261, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(270, 320, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 510, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(380, 510, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")


        #senha usada na transferencia
        #label
        self.label_senha = QtWidgets.QLabel(Form)
        self.label_senha.setGeometry(QtCore.QRect(6, 200, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_senha.setFont(font)
        self.label_senha.setObjectName("label_2")
        self.label_senha.move(150,300)

        #line edit
        self.lineEdit_senha = QtWidgets.QLineEdit(Form)
        self.lineEdit_senha.setGeometry(QtCore.QRect(230, 190, 261, 31))
        self.lineEdit_senha.setObjectName("lineEdit")
        self.lineEdit_senha.move(230,300)
        

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Transferir"))
        self.label_2.setText(_translate("Form", "login conta destino"))
        self.label_3.setText(_translate("Form", "Valor  a transferir"))
        self.lineEdit.setPlaceholderText(_translate("Form", "    Login do cliente para transferir "))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "    Valor para transferir"))
        #line edit senha nova criada para a tela
        self.lineEdit_senha.setPlaceholderText(_translate("Form","   Sua senha"))
        #label senha
        self.label_senha.setText(_translate("Form", "Senha"))

        self.pushButton.setText(_translate("Form", "Transferir"))
        #movendo botão de transferir para abrir espaço na tela
        self.pushButton.move(250,400)
        self.pushButton_2.setText(_translate("Form", "Voltar"))
        self.pushButton_3.setText(_translate("Form", "Sair"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Tela_Transferir()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
