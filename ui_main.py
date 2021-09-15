from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtGui
from PySide2.QtGui import QIcon
import os
#self.pushButton.clicked.connect(botao1)                #self.pushButton_2 ##1   
#self.pushButton_2.clicked.connect(botao2)              #self.pushButton_7 ##2
#self.pushButton_3.clicked.connect(botao3)              #self.pushButton_5  ##3
#self.pushButton_5.clicked.connect(botao4)              #self.pushButton_8  ##4
#self.pushButton_7.clicked.connect(botao6)              #self.pushButton_6  ##5
#self.pushButton_6.clicked.connect(botao5)              #self.pushButton_3  ##6
#self.pushButton_8.clicked.connect(botao7)              #self.pushButton_10  ##7
#self.pushButton_9.clicked.connect(botao8)              
#self.pushButton_10.clicked.connect(botao9)             #self.pushButton_9 ##8
#self.pushButton_11.clicked.connect(botao10)            #self.pushButton_11 ##9

def botao1(self):
        os.system("start chrome /incognito https://www.patreon.com/rafaelrochar")

def botao2(self):
        os.system("Reg Add HKCU\Software\Microsoft\Windows\CurrentVersion\BackgroundAccessApplications /v GlobalUserDisabled /t REG_DWORD /d 1 /f")
        os.system("sc config “DiagTrack” start= disabled")

def botao3(self):
        os.system("powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61")
        os.system("start DESEMPENHO.pdf")

def botao4(self):
        os.system("start windowsdefender.txt")

def botao5(self):
        os.system("clovao.txt")

def botao6(self):
        os.system("start /B start cmd.exe @cmd /k sfc /scannow && DISM.exe /Online /Cleanup-image /Restorehealth")

def botao7(self):
        os.system("start dicas.txt && Taskmgr.exe")
        os.system("exit")

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"Janela Principal")
        MainWindow.setWindowIcon(QtGui.QIcon('UP.jpg'))
        MainWindow.resize(574, 430)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(115, 80, 163);\n")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 120, 181, 131))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"QPushButton {background-color: rgb(170, 85, 255, 255)}"
        "QPushButton:pressed {background-color: rgb(138, 69, 207)}"
        "QPushButton {border-style: none}"
        "QPushButton {border-radius: 10px}"
        "QPushButton {border-radius: 10px}")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 10, 551, 51))
        font1 = QFont()
        font1.setFamily(u"Segoe UI Black")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"QPushButton {background-color: rgb(170, 85, 255, 255)}"
        "QPushButton:pressed {background-color: rgb(138, 69, 207)}"
        "QPushButton {border-style: none}"
        "QPushButton {border-radius: 10px}"
        "QPushButton {border-radius: 10px}")
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(390, 310, 171, 31))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet(u"QPushButton {background-color: rgb(205, 84, 255)}"
        "QPushButton:pressed {background-color: rgb(168, 94, 200)}"
        "QPushButton {border-style: none}"
        "QPushButton {border-radius: 10px}"
        "QPushButton {border-radius: 10px}")
        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(380, 120, 181, 131))
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet(u"QPushButton {background-color: rgb(170, 85, 255, 255)}"
        "QPushButton:pressed {background-color: rgb(138, 69, 207)}"
        "QPushButton {border-style: none}"
        "QPushButton {border-radius: 10px}"
        "QPushButton {border-radius: 10px}")
        self.pushButton_6 = QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(200, 310, 171, 31))
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet(u"QPushButton {background-color: rgb(205, 84, 255)}"
        "QPushButton:pressed {background-color: rgb(168, 94, 200)}"
        "QPushButton {border-style: none}"
        "QPushButton {border-radius: 10px}"
        "QPushButton {border-radius: 10px}")
        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(200, 120, 171, 131))
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet(u"QPushButton {background-color: rgb(170, 85, 255, 255)}"
        "QPushButton:pressed {background-color: rgb(138, 69, 207)}"
        "QPushButton {border-style: none}"
        "QPushButton {border-radius: 10px}"
        "QPushButton {border-radius: 10px}")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 70, 291, 31))
        font2 = QFont()
        font2.setFamily(u"Segoe UI Historic")
        font2.setPointSize(20)
        font2.setBold(False)
        font2.setWeight(50)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 260, 351, 31))
        self.label_2.setFont(font2)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(20, 310, 161, 31))
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet(u"QPushButton {background-color: rgb(205, 84, 255)}"
        "QPushButton:pressed {background-color: rgb(168, 94, 200)}"
        "QPushButton {border-style: none}"
        "QPushButton {border-radius: 10px}"
        "QPushButton {border-radius: 10px}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 574, 21))
        self.menuPor_favor_selecione_uma_op_o = QMenu(self.menubar)
        self.menuPor_favor_selecione_uma_op_o.setObjectName(u"menuPor_favor_selecione_uma_op_o")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(botao1) ##botao patreon
        self.pushButton_2.clicked.connect(botao2)
        self.pushButton_3.clicked.connect(botao3)
        self.pushButton_5.clicked.connect(botao4)
        self.pushButton_6.clicked.connect(botao5)
        self.pushButton_7.clicked.connect(botao6)
        self.pushButton_8.clicked.connect(botao7)

        self.pushButton.setToolTip("Ao clicar aqui você será redirecionado para uma página para apoiar\n   com dinheiro real o trabalho do criador desse programa")
        self.pushButton_2.setToolTip("Esse botão desativa a opção de aplicativos de segundo plano no computador\nO que não faz falta no dia a dia e ajuda muito a acelerar o processamento do computador") ##1
        self.pushButton_7.setToolTip("Esse botão abrirá duas janelas do CMD e iniciará dois processos para checar se existe algum arquivo corrompido\natrapalhando o funcionamento dos processos do windows e, se tiver, irá consertá-lo") ##2
        self.pushButton_5.setToolTip("Esse botão abrirá um .txt explicando como resolver o problema do windows usando muito disco") ##3
        self.pushButton_8.setToolTip("Esse botão abre um bloco de notas e o gerenciador de tarefas. No bloco de notas você encontrará algumas instruções sobre o que fazer\nno gerenciador de tarefas e dicas para melhorar o desempenho do computador") ##4
        self.pushButton_3.setToolTip("Esse botão liberará o modo de desempenho no seu computador e irá te ensinsar a ativar esse modo") ##6
        self.pushButton_6.setToolTip("Você não conhece o Clovão????")
        self.menubar.addAction(self.menuPor_favor_selecione_uma_op_o.menuAction())
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("Janela Principal", u"Janela Principal", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Problemas mais comuns", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Problemas menos comuns", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Considere contribuir para o or\u00e7amento de futuros projetos como esse", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PC lento", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Processo\nusando\nmuito disco", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Windows Defender\nespecíficamente\nusando muito disco", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"PC continua lento", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Melhorar p/ jogos", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Clovão!", None))
        self.menuPor_favor_selecione_uma_op_o.setTitle(QCoreApplication.translate("MainWindow", u"Por favor selecione uma op\u00e7\u00e3o || Deixe o mouse acima do botão para saber o que ele faz", None))

