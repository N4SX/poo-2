import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication

from tela_inicial import Tela_Inicial
from tela_menu import Tela_Menu
from tela_cadastro import Tela_Cadastro
from tela_deposito import Tela_Deposito
from tela_sacar import Tela_Sacar
from tela_transferir import Tela_Transferir
from tela_extrato import Tela_Extrato
from banco import *

acc_atual = ''

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Ui_Main')
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()  
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()
        self.stack7 = QtWidgets.QMainWindow()

        self.tela_inicial = Tela_Inicial()
        self.tela_inicial.setupUi(self.stack0)

        self.tela_menu = Tela_Menu()
        self.tela_menu.setupUi(self.stack1)

        self.tela_cadastro = Tela_Cadastro()
        self.tela_cadastro.setupUi(self.stack2)

        self.tela_deposito = Tela_Deposito()
        self.tela_deposito.setupUi(self.stack3)

        self.tela_saque = Tela_Sacar()
        self.tela_saque.setupUi(self.stack4)

        self.tela_transferir = Tela_Transferir()
        self.tela_transferir.setupUi(self.stack5)

        self.tela_extrato = Tela_Extrato()
        self.tela_extrato.setupUi(self.stack6)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)

class Main(QMainWindow, Ui_Main):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.b = Banco()        
        #tela inicial
        self.tela_inicial.pushButton.clicked.connect(self.botao_login)
        self.tela_inicial.pushButton_2.clicked.connect(self.abrirCadastro)
        self.tela_inicial.pushButton_3.clicked.connect(self.sair)
        #tela cadastro
        self.tela_cadastro.pushButton.clicked.connect(self.botao_cadastra)
        self.tela_cadastro.pushButton_2.clicked.connect(self.voltarTelaInicial)
        self.tela_cadastro.pushButton_3.clicked.connect(self.sair)
        #tela menu(usuario pós login)
        self.tela_menu.pushButton.clicked.connect(self.abrirTelaDeposito)
        self.tela_menu.pushButton_2.clicked.connect(self.abrirTelaSaque)
        self.tela_menu.pushButton_3.clicked.connect(self.abrirTelaTransfere)
        self.tela_menu.pushButton_4.clicked.connect(self.abrirTelaExtrato)
        self.tela_menu.pushButton_5.clicked.connect(self.sair)
        self.tela_menu.pushButton_6.clicked.connect(self.voltarTelaInicial)
        #tela deposita
        self.tela_deposito.pushButton.clicked.connect(self.botao_deposito)
        self.tela_deposito.pushButton_2.clicked.connect(self.abrirTelaMenu)
        self.tela_deposito.pushButton_3.clicked.connect(self.sair)
        #tela sacar
        self.tela_saque.pushButton.clicked.connect(self.botao_saque)
        self.tela_saque.pushButton_2.clicked.connect(self.abrirTelaMenu)
        self.tela_saque.pushButton_3.clicked.connect(self.sair)
        #tela transfere
        self.tela_transferir.pushButton.clicked.connect(self.botao_transferir)
        self.tela_transferir.pushButton_2.clicked.connect(self.abrirTelaMenu)
        self.tela_transferir.pushButton_3.clicked.connect(self.sair)
        #tela extrato
        self.tela_extrato.pushButton.clicked.connect(self.abrirTelaMenu)
        self.tela_extrato.pushButton_2.clicked.connect(self.sair)

        
    def botao_login(self):
        usuario = self.tela_inicial.lineEdit.text()
        senha = self.tela_inicial.lineEdit_2.text()

        if not(usuario == '' or senha == ''):
            if confirma_login(usuario,senha,self.b):
                global acc_atual
                acc_atual = usuario
                self.abrirTelaMenu(usuario)
            else:
                QMessageBox().warning(None,'N-BANK','Usuario/Senha incorreto!')    
        else:
            QMessageBox().warning(None,'N-BANK','Todos os campos devem ser preenchidos')
    
    def botao_cadastra(self):
        # usuario == login
        usuario = self.tela_cadastro.lineEdit.text()
        senha = self.tela_cadastro.lineEdit_2.text()
        nome = self.tela_cadastro.lineEdit_3.text()
        cpf = self.tela_cadastro.lineEdit_4.text()

        # se todos os campos estiverem preenchidos a operação acontecerá
        if not(usuario == '' or senha == '' or nome == '' or cpf == ''):
            c = Cliente(nome,cpf)
            cc = Conta(gera_numero(self.b),c,senha,usuario)
            #se foi possivel salvar o cliente e a conta no banco usando o login como chave primária
            if self.b.adiciona_cliente(c,usuario) and self.b.adiciona_conta(cc,usuario):
                self.tela_cadastro.lineEdit.setText('')
                self.tela_cadastro.lineEdit_2.setText('')
                self.tela_cadastro.lineEdit_3.setText('')
                self.tela_cadastro.lineEdit_4.setText('')
            else:
                QMessageBox().warning(None,'N-BANK','Login já cadastrado')
                    
        else:
            QMessageBox().warning(None,'N-BANK','Todos os campos devem ser preenchidos')
    
    def botao_deposito(self):
        valor = self.tela_deposito.lineEdit.text()
        if not(valor == ''):
            if self.b.contas[acc_atual].deposita(float(valor)):
                QMessageBox().information(None,'N-BANK','Depósito realizado com sucesso!')
                self.tela_deposito.lineEdit.setText('')
            else:
                QMessageBox().warning(None,'N-BANK','Falha na operação!')
        else:
            QMessageBox().warning(None,'N-BANK','Todos os campos devem ser preenchidos')
    
    def botao_saque(self):
        senha = self.tela_saque.lineEdit.text()
        valor = self.tela_saque.lineEdit_2.text()
        if not(senha == '' and valor == ''):
            if self.b.contas[acc_atual].saque(float(valor), senha):
                QMessageBox().information(None,'N-BANK','Saque realizado com sucesso!')
                self.tela_saque.lineEdit.setText('')
                self.tela_saque.lineEdit_2.setText('')
            else:
                QMessageBox().warning(None,'N-BANK','Falha na operação!')
        else:     
            QMessageBox().warning(None,'N-BANK','Todos os campos devem ser preenchidos')
    
    def botao_transferir(self):
        login = self.tela_transferir.lineEdit.text()
        valor = self.tela_transferir.lineEdit_2.text()
        senha = self.tela_transferir.lineEdit_senha.text()
        if not(login == '' or valor == '' or senha == ''):
            conta_destino = self.b.busca_conta(login)
            print(conta_destino.saldo)
            if not(conta_destino == None):
                if self.b.contas[acc_atual].transfere(conta_destino, float(valor), senha):
                    QMessageBox().information(None,'N-BANK','Transferência realizada com sucesso!')
                    self.tela_transferir.lineEdit.setText('')
                    self.tela_transferir.lineEdit_2.setText('')
                    self.tela_transferir.lineEdit_senha.setText('')
                else:
                    QMessageBox().information(None,'N-BANK','Falha na operação!')
            else:
                QMessageBox().warning(None,'N-BANK','Login Invalido!')
        else:
            QMessageBox().warning(None,'N-BANK','Todos os campos devem ser preenchidos')        
    
    def abrirCadastro(self):
        self.QtStack.setCurrentIndex(2)
    
    def abrirInicial(self):
        self.QtStack.setCurrentIndex(0)
    
    def abrirTelaMenu(self, l):
        self.QtStack.setCurrentIndex(1)

    def abrirTelaExtrato(self):
        self.QtStack.setCurrentIndex(6)
        QMessageBox().information(None,'N-BANK','Extrato gerado!')
        self.tela_extrato.extrato.setText((self.b.contas[acc_atual].get_historico).imprime(self.b.contas[acc_atual]))
    def abrirTelaDeposito(self):
        self.QtStack.setCurrentIndex(3)
    def abrirTelaSaque(self):
        self.QtStack.setCurrentIndex(4)
    def abrirTelaTransfere(self):
        self.QtStack.setCurrentIndex(5)
	
    def sair(self):
        sys.exit(app.exec_())
    def voltarTelaInicial(self):
        self.QtStack.setCurrentIndex(0)
    def voltarTelaUsuario(self):
        self.QtStack.setCurrentIndex(2)

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())  