import sys
import os
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,  QDialog, QFileDialog, QButtonGroup
from PyQt5.QtGui import QPixmap

from cryption import aes_256_encrypted, aes_256_decrypted
from hash_code import md_5, sha_1, sha_3, custom_hash


class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(360, 505)
        MainWindow.setMinimumSize(QtCore.QSize(360, 505))
        MainWindow.setMaximumSize(QtCore.QSize(360, 505))
        MainWindow.setStyleSheet("background-color:#c19a6b")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonFollowStyle)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_main = QtWidgets.QFrame(self.centralwidget)
        self.frame_main.setGeometry(QtCore.QRect(0, -20, 361, 181))
        self.frame_main.setStyleSheet("background-color:#e0ccb4")
        self.frame_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setObjectName("frame_main")
        self.label_shif = QtWidgets.QLabel(self.frame_main)
        self.label_shif.setGeometry(QtCore.QRect(110, 20, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(20)
        self.label_shif.setFont(font)
        self.label_shif.setStyleSheet("color:black")
        self.label_shif.setObjectName("label_shif")
        self.label_2 = QtWidgets.QLabel(self.frame_main)
        self.label_2.setScaledContents(True)
        self.label_2.setPixmap(QPixmap("Imgs/Шифратор.png"))
        self.label_2.setGeometry(QtCore.QRect(110, 60, 130, 120))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(10, 190, 341, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setAcceptDrops(True)
        self.pushButton_1.setStyleSheet("QPushButton{\n"
                                        "    color: black;\n"
                                        "    background-color:#b85d43;\n"
                                        "    border-radius:30;\n"
                                        "    border:2px solid\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed{\n"
                                        "    background-color:#6e3727;\n"
                                        "}")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 260, 341, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setAcceptDrops(True)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "    color: black;\n"
                                        "    background-color:#b85d43;\n"
                                        "    border-radius:30;\n"
                                        "    border:2px solid\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed{\n"
                                        "    background-color:#6e3727;\n"
                                        "}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 330, 341, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setAcceptDrops(True)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
                                        "    color: black;\n"
                                        "    background-color:#b85d43;\n"
                                        "    border-radius:30;\n"
                                        "    border:2px solid\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed{\n"
                                        "    background-color:#6e3727;\n"
                                        "}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 400, 341, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setAcceptDrops(True)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
                                        "    color: black;\n"
                                        "    background-color:#b85d43;\n"
                                        "    border-radius:30;\n"
                                        "    border:2px solid\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed{\n"
                                        "    background-color:#6e3727;\n"
                                        "}")
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 360, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setStatusTip("")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actiondf = QtWidgets.QAction(MainWindow)
        self.actiondf.setObjectName("actiondf")
        self.menu_1 = QtWidgets.QAction(MainWindow)
        self.menu_1.setObjectName("menu_1")
        self.menu_2 = QtWidgets.QAction(MainWindow)
        self.menu_2.setObjectName("menu_2")
        self.menuMenu.addAction(self.menu_1)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.menu_2)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Шифратор"))
        self.label_shif.setText(_translate("MainWindow", "Шифратор"))
        self.pushButton_1.setText(_translate("MainWindow", "Зашифровать AES-256"))
        self.pushButton_2.setText(_translate("MainWindow", "Расшифровать AES-256"))
        self.pushButton_3.setText(_translate("MainWindow", "Хэшировать"))
        self.pushButton_4.setText(_translate("MainWindow", "Удалить из базы"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actiondf.setText(_translate("MainWindow", "df"))
        self.menu_1.setText(_translate("MainWindow", "Открыть расположение программы"))
        self.menu_2.setText(_translate("MainWindow", "Помощь"))


class MainLogic(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_1.clicked.connect(lambda x: self.button_do(1))
        self.pushButton_2.clicked.connect(lambda x: self.button_do(2))
        self.pushButton_3.clicked.connect(lambda x: self.button_do(3))
        self.pushButton_4.clicked.connect(lambda x: self.button_do(4))

        self.menu_1.triggered.connect(lambda x: self.menu_do(1))
        self.menu_2.triggered.connect(lambda x: self.menu_do(2))

    def button_do(self, number):  # Переход в другие окна
        if number == 1:
            self.EncryptLogic = EncryptLogic()
            self.EncryptLogic.show()
            self.hide()

        elif number == 2:
            self.DecryptionLogic = DecryptionLogic()
            self.DecryptionLogic.show()
            self.hide()

        elif number == 3:
            self.HashLogic = HashLogic()
            self.HashLogic.show()
            self.hide()
        elif number == 4:
            self.PasswordDelLogic = PasswordDelLogic()
            self.PasswordDelLogic.show()
            self.hide()

    def menu_do(self, number):  # Логика для кнопки меню
        if number == 1:
            path = os.getcwd()
            os.startfile(path)
            print(path)
        elif number == 2:
            path = os.getcwd()
            os.startfile(path + r'\README.txt')


class Encrypt(QMainWindow):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(490, 274)
        Dialog.setStyleSheet("background-color:#c19a6b")
        self.pushButton_choice_file = QtWidgets.QPushButton(Dialog)
        Dialog.setMinimumSize(QtCore.QSize(490, 274))
        Dialog.setMaximumSize(QtCore.QSize(490, 274))
        self.pushButton_choice_file.setGeometry(QtCore.QRect(10, 120, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_choice_file.setFont(font)
        self.pushButton_choice_file.setAcceptDrops(True)
        self.pushButton_choice_file.setStyleSheet("QPushButton{\n"
                                                  "    color: black;\n"
                                                  "    background-color:#b85d43;\n"
                                                  "    border-radius:30;\n"
                                                  "    border:2px solid\n"
                                                  "}\n"
                                                  "\n"
                                                  "QPushButton:pressed{\n"
                                                  "    background-color:#6e3727;\n"
                                                  "}")
        self.pushButton_choice_file.setObjectName("pushButton_choice_file")

        self.lineEdit_pasword = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_pasword.setGeometry(QtCore.QRect(10, 20, 471, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_pasword.setFont(font)
        self.lineEdit_pasword.setStyleSheet("color: black;\n"
                                            "border:2px solid;\n"
                                            "background-color:white;")
        self.lineEdit_pasword.setText("")
        self.lineEdit_pasword.setObjectName("lineEdit_pasword")

        self.lineEdit_directory = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_directory.setGeometry(QtCore.QRect(10, 70, 471, 41))
        self.lineEdit_directory.setFont(font)
        self.lineEdit_directory.setStyleSheet("color: black;\n"
                                              "border:2px solid;\n"
                                              "background-color:white;")
        self.lineEdit_directory.setText("")
        self.lineEdit_directory.setReadOnly(False)
        self.lineEdit_directory.setObjectName("lineEdit_directory")

        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_crypted = QtWidgets.QPushButton(Dialog)
        self.pushButton_crypted.setGeometry(QtCore.QRect(10, 190, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_crypted.setFont(font)
        self.pushButton_crypted.setAcceptDrops(True)
        self.pushButton_crypted.setStyleSheet("QPushButton{\n"
                                              "    color: black;\n"
                                              "    background-color:#b85d43;\n"
                                              "    border-radius:30;\n"
                                              "    border:2px solid\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:pressed{\n"
                                              "    background-color:#6e3727;\n"
                                              "}")
        self.pushButton_crypted.setObjectName("pushButton_crypted")
        self.pushButton_back = QtWidgets.QPushButton(Dialog)
        self.pushButton_back.setGeometry(QtCore.QRect(330, 220, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_back.setFont(font)
        self.pushButton_back.setAcceptDrops(True)
        self.pushButton_back.setStyleSheet("QPushButton{\n"
                                           "    color: black;\n"
                                           "    background-color:#b85d43;\n"
                                           "    border-radius:30;\n"
                                           "    border:2px solid\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "    background-color:#6e3727;\n"
                                           "}")
        self.pushButton_back.setObjectName("pushButton_back")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setPixmap(QPixmap("Imgs/Back.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setGeometry(QtCore.QRect(430, 220, 41, 31))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Зашифровать"))
        self.pushButton_choice_file.setText(_translate("Dialog", "Выбрать файл"))
        self.lineEdit_pasword.setPlaceholderText(_translate("Dialog", "Пароль"))
        self.lineEdit_directory.setPlaceholderText(_translate("Dialog", "Путь"))
        self.pushButton_crypted.setText(_translate("Dialog", "Зашифровать"))
        self.pushButton_back.setText(_translate("Dialog", "Назад"))


class EncryptLogic(Encrypt, QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.pushButton_back.clicked.connect(self.back_do)
        self.pushButton_crypted.clicked.connect(self.crypted_do)
        self.pushButton_choice_file.clicked.connect(self.choise_file)

    def back_do(self):  # Возвращение в главное окно
        self.close()
        global ex
        ex.setVisible(True)

    def choise_file(self):  # Выбор файла в windows
        fname = str(QFileDialog.getOpenFileName()[0])
        self.lineEdit_directory.setText(fname)

    def crypted_do(self):  # Функционал кнопки шифрования
        try:  # Проверка на ошибки связанные с выбором файла
            password = self.lineEdit_pasword.text()
            if not password is None:
                con = sqlite3.connect("DataBaseP1.db")
                cur = con.cursor()
                x = cur.execute(f"""SELECT * FROM Crypt2 WHERE password == '{str(md_5(str(password)))}'""").fetchall()
                if len(x) != 0:  # Проверка пароля для избежания коллизии
                    self.lineEdit_pasword.setText('Пароль уже используется')
                    return
                fname = QFileDialog.getSaveFileName(filter='txt')[0]
                file = open(self.lineEdit_directory.text()).read()

                salt = aes_256_encrypted(file, password, fname + '.txt')
                cur.execute(f"""INSERT INTO Crypt2(password, salt)
                                 VALUES('{str(md_5(str(password)))}', ?)""", (salt, ))  # Добавление Хэш и salt в БД
                con.commit()
                cur.close()
        except Exception:
            self.lineEdit_directory.setText('Некорректный путь')


class HashQt(QMainWindow):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(490, 600)
        Dialog.setMinimumSize(QtCore.QSize(490, 600))
        Dialog.setMaximumSize(QtCore.QSize(490, 600))
        Dialog.setStyleSheet("background-color:#c19a6b")
        self.pushButton_choice_file = QtWidgets.QPushButton(Dialog)
        self.pushButton_choice_file.setGeometry(QtCore.QRect(10, 180, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_choice_file.setFont(font)
        self.pushButton_choice_file.setAcceptDrops(True)
        self.pushButton_choice_file.setStyleSheet("QPushButton{\n"
                                                  "    color: black;\n"
                                                  "    background-color:#b85d43;\n"
                                                  "    border-radius:30;\n"
                                                  "    border:2px solid\n"
                                                  "}\n"
                                                  "\n"
                                                  "QPushButton:pressed{\n"
                                                  "    background-color:#6e3727;\n"
                                                  "}")
        self.pushButton_choice_file.setObjectName("pushButton_choice_file")
        self.pushButton_hash = QtWidgets.QPushButton(Dialog)
        self.pushButton_hash.setGeometry(QtCore.QRect(10, 530, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_hash.setFont(font)
        self.pushButton_hash.setAcceptDrops(True)
        self.pushButton_hash.setStyleSheet("QPushButton{\n"
                                            "    color: black;\n"
                                            "    background-color:#b85d43;\n"
                                            "    border-radius:30;\n"
                                            "    border:2px solid\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:pressed{\n"
                                            "    background-color:#6e3727;\n"
                                            "}")
        self.pushButton_hash.setObjectName("pushButton_hash")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 40, 471, 131))
        self.plainTextEdit.setStyleSheet("background-color:white;\n"
                                         "border-color:black;\n"
                                         "border: 2px solid;")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.text_b2 = QtWidgets.QLabel(Dialog)
        self.text_b2.setGeometry(QtCore.QRect(10, 10, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.text_b2.setFont(font)
        self.text_b2.setStyleSheet("color:black\n""")
        self.text_b2.setObjectName("text_b2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(440, 560, 41, 31))
        self.label_2.setPixmap(QPixmap("Imgs/Back.png"))
        self.label_2.setText("")
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.pushButton_back = QtWidgets.QPushButton(Dialog)
        self.pushButton_back.setGeometry(QtCore.QRect(340, 560, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_back.setFont(font)
        self.pushButton_back.setAcceptDrops(True)
        self.pushButton_back.setStyleSheet("QPushButton{\n"
                                           "    color: black;\n"
                                           "    background-color:#b85d43;\n"
                                           "    border-radius:30;\n"
                                           "    border:2px solid\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "    background-color:#6e3727;\n"
                                           "}")
        self.pushButton_back.setObjectName("pushButton_back")
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(410, 290, 58, 136))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.verticalLayoutWidget.setFont(font)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.B_224 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.B_224.setFont(font)
        self.B_224.setStyleSheet("color:black\n""")
        self.B_224.setObjectName("B_224")
        self.verticalLayout.addWidget(self.B_224)
        self.B_256 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.B_256.setFont(font)
        self.B_256.setObjectName("B_256")
        self.verticalLayout.addWidget(self.B_256)
        self.B_384 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.B_384.setFont(font)
        self.B_384.setObjectName("B_384")
        self.verticalLayout.addWidget(self.B_384)
        self.B_512 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.B_512.setFont(font)
        self.B_512.setObjectName("B_512")
        self.verticalLayout.addWidget(self.B_512)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(40, 260, 111, 168))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.verticalLayoutWidget_2.setFont(font)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.B_sha1 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.B_sha1.setFont(font)
        self.B_sha1.setStyleSheet("color:black\n""")
        self.B_sha1.setObjectName("B_sha1")
        self.verticalLayout_2.addWidget(self.B_sha1)
        self.B_sha3 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.B_sha3.setFont(font)
        self.B_sha3.setObjectName("B_sha3")
        self.verticalLayout_2.addWidget(self.B_sha3)
        self.B_md5 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.B_md5.setFont(font)
        self.B_md5.setObjectName("B_md5")
        self.verticalLayout_2.addWidget(self.B_md5)
        self.B_custom = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.B_custom.setFont(font)
        self.B_custom.setObjectName("B_custom")
        self.verticalLayout_2.addWidget(self.B_custom)
        self.text_b1 = QtWidgets.QLabel(Dialog)
        self.text_b1.setGeometry(QtCore.QRect(340, 260, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.text_b1.setFont(font)
        self.text_b1.setStyleSheet("color:black\n""")
        self.text_b1.setObjectName("text_b1")
        self.lineEdit_result = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_result.setGeometry(QtCore.QRect(10, 470, 471, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_result.setFont(font)
        self.lineEdit_result.setStyleSheet("color: black;\n""border:2px solid;\n""background-color:white;")
        self.lineEdit_result.setText("")
        self.lineEdit_result.setReadOnly(True)
        self.lineEdit_result.setPlaceholderText("")
        self.lineEdit_result.setObjectName("lineEdit_result")
        self.checkBox = QtWidgets.QCheckBox(Dialog)
        self.checkBox.setGeometry(QtCore.QRect(240, 200, 301, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Хэширование"))
        self.pushButton_choice_file.setText(_translate("Dialog", "Выбрать файл"))
        self.pushButton_hash.setText(_translate("Dialog", "Хэшировать"))
        self.text_b2.setText(_translate("Dialog", "Введите текст или выберите файл:"))
        self.pushButton_back.setText(_translate("Dialog", "Назад"))
        self.B_224.setText(_translate("Dialog", "224"))
        self.B_256.setText(_translate("Dialog", "256"))
        self.B_384.setText(_translate("Dialog", "384"))
        self.B_512.setText(_translate("Dialog", "512"))
        self.B_sha1.setText(_translate("Dialog", "sha-1"))
        self.B_sha3.setText(_translate("Dialog", "sha-3"))
        self.B_md5.setText(_translate("Dialog", "md5"))
        self.B_custom.setText(_translate("Dialog", "custom"))
        self.text_b1.setText(_translate("Dialog", "sha-1 и sha-3"))
        self.checkBox.setText(_translate("Dialog", "Сохранить в Базе Данных"))


class HashLogic(HashQt, QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.file = None

        self.pushButton_back.clicked.connect(self.back_do)
        self.pushButton_choice_file.clicked.connect(self.choise_file)
        self.pushButton_hash.clicked.connect(self.hash_do)

        self.button_group_type = QButtonGroup()
        self.button_group_type.addButton(self.B_sha1)
        self.button_group_type.addButton(self.B_sha3)
        self.button_group_type.addButton(self.B_custom)
        self.button_group_type.addButton(self.B_md5)

        self.button_group_by = QButtonGroup()
        self.button_group_by.addButton(self.B_224)
        self.button_group_by.addButton(self.B_256)
        self.button_group_by.addButton(self.B_384)
        self.button_group_by.addButton(self.B_512)

    def hash_do(self):
        def clear():
            self.file = None
            self.plainTextEdit.setDisabled(False)

        def sha13(): # Проверка выбрана ли разрядность
            try:
                return self.button_group_by.checkedButton().text()
            except Exception:
                clear()
                self.lineEdit_result.setText('Выберите разряд')
                return

        text = ''
        """Получение текста для шифрования"""
        try:
            if self.file is None:
                text = self.plainTextEdit.toPlainText()
            else:
                text = open(self.file).read()
        except Exception:
            self.plainTextEdit.setPlainText('Некорректный путь')

        type1 = ''
        type2 = ''

        try:
            type1 = self.button_group_type.checkedButton().text()
        except Exception:
            clear()
            self.lineEdit_result.setText('Выберите тип')

        """Хэширование с проверкой"""
        result = ''
        if type1 == 'sha-1':
            type2 = sha13()
            if type2:
                result = sha_1(text, type2)
            else:
                self.lineEdit_result.setText('Выберите разряд')
                clear()
                return
        elif type1 == 'sha-3':
            type2 = sha13()
            if type2:
                result = sha_3(text, type2)
            else:
                self.lineEdit_result.setText('Выберите разряд')
                clear()
                return
        elif type1 == 'md5':
            result = md_5(text)
        elif type1 == 'custom':
            result = custom_hash(text)
        else:
            clear()
            return

        if self.checkBox.isChecked():
            con = sqlite3.connect("DataBaseP1.db")
            cur = con.cursor()
            x = cur.execute(f"""SELECT id FROM HashType2 WHERE type == "{type1}"
             OR type LIKE "{type1.replace('-', '') + '(' + type2 + ')'}" """).fetchall()[0][0]
            cur.execute(f"""INSERT INTO TableHash2(hash, type, text)
                                             VALUES('{result}', '{x}', '{text}')""")
            con.commit()
            cur.close()

        self.lineEdit_result.setText(result)
        clear()

    def choise_file(self):  # Получение ссылки на файл
        fname = str(QFileDialog.getOpenFileName()[0])
        self.file = fname
        self.plainTextEdit.setPlainText(fname)
        self.plainTextEdit.setDisabled(True)

    def back_do(self):  # Возвращение в главное окно
        self.close()
        global ex
        ex.setVisible(True)


class Decryption(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(490, 480)
        Dialog.setMinimumSize(QtCore.QSize(490, 480))
        Dialog.setMaximumSize(QtCore.QSize(490, 480))
        Dialog.setStyleSheet("background-color:#c19a6b\n""")
        self.pushButton_decrypted = QtWidgets.QPushButton(Dialog)
        self.pushButton_decrypted.setGeometry(QtCore.QRect(250, 120, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_decrypted.setFont(font)
        self.pushButton_decrypted.setAcceptDrops(True)
        self.pushButton_decrypted.setStyleSheet("QPushButton{\n"
                                                "    color: black;\n"
                                                "    background-color:#b85d43;\n"
                                                "    border-radius:30;\n"
                                                "    border:2px solid\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:pressed{\n"
                                                "    background-color:#6e3727;\n"
                                                "}")
        self.pushButton_decrypted.setObjectName("pushButton_decrypted")
        self.pushButton_choice_file = QtWidgets.QPushButton(Dialog)
        self.pushButton_choice_file.setGeometry(QtCore.QRect(10, 120, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_choice_file.setFont(font)
        self.pushButton_choice_file.setAcceptDrops(True)
        self.pushButton_choice_file.setStyleSheet("QPushButton{\n"
                                                  "    color: black;\n"
                                                  "    background-color:#b85d43;\n"
                                                  "    border-radius:30;\n"
                                                  "    border:2px solid\n"
                                                  "}\n"
                                                  "\n"
                                                  "QPushButton:pressed{\n"
                                                  "    background-color:#6e3727;\n"
                                                  "}")
        self.pushButton_choice_file.setObjectName("pushButton_choice_file")
        self.lineEdit_pasword = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_pasword.setGeometry(QtCore.QRect(10, 20, 471, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_pasword.setFont(font)
        self.lineEdit_pasword.setStyleSheet("color: black;\n"
                                            "border:2px solid;\n"
                                            "background-color:white;")
        self.lineEdit_pasword.setText("")
        self.lineEdit_pasword.setObjectName("lineEdit_pasword")
        self.pushButton_back = QtWidgets.QPushButton(Dialog)
        self.pushButton_back.setGeometry(QtCore.QRect(340, 440, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_back.setFont(font)
        self.pushButton_back.setAcceptDrops(True)
        self.pushButton_back.setStyleSheet("QPushButton{\n"
                                           "    color: black;\n"
                                           "    background-color:#b85d43;\n"
                                           "    border-radius:30;\n"
                                           "    border:2px solid\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "    background-color:#6e3727;\n"
                                           "}")
        self.pushButton_back.setObjectName("pushButton_back")
        self.lineEdit_directory = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_directory.setGeometry(QtCore.QRect(10, 70, 471, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_directory.setFont(font)
        self.lineEdit_directory.setStyleSheet("color: black;\n"
                                              "border:2px solid;\n"
                                              "background-color:white;")
        self.lineEdit_directory.setText("")
        self.lineEdit_directory.setReadOnly(False)
        self.lineEdit_directory.setObjectName("lineEdit_directory")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(440, 440, 41, 31))
        self.label.setText("")
        self.label.setPixmap(QPixmap("Imgs/Back.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 200, 471, 221))
        self.plainTextEdit.setStyleSheet("background-color:white;\n"
                                         "border-color:black;\n"
                                         "border: 2px solid;")
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Расшифратор"))
        self.pushButton_decrypted.setText(_translate("Dialog", "Расшифровать"))
        self.pushButton_choice_file.setText(_translate("Dialog", "Выбрать файл"))
        self.lineEdit_pasword.setPlaceholderText(_translate("Dialog", "Пароль"))
        self.pushButton_back.setText(_translate("Dialog", "Назад"))
        self.lineEdit_directory.setPlaceholderText(_translate("Dialog", "Путь"))


class DecryptionLogic(Decryption, QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.file = None

        self.pushButton_back.clicked.connect(self.back_do)
        self.pushButton_choice_file.clicked.connect(self.choise_file)
        self.pushButton_decrypted.clicked.connect(self.decrypt)

    def decrypt(self):  # Расшифровка
        passwordH = str(md_5(self.lineEdit_pasword.text()))
        con = sqlite3.connect("DataBaseP1.db")
        cur = con.cursor()
        try:  # Есть ли пароль в БД
            x = cur.execute(f"""SELECT salt FROM Crypt2 WHERE password == '{passwordH}'""").fetchall()[0][0]
        except Exception:
            x = []
        result = ''

        """Расшифровка с проверкой на путь и пароль"""
        if len(x) != 0:
            try:
                result = aes_256_decrypted(self.lineEdit_directory.text(), self.lineEdit_pasword.text(), x)
            except Exception:
                self.plainTextEdit.setPlaceholderText('Некорректный путь')
        else:
            self.plainTextEdit.setPlaceholderText('Некорректный пароль')
        self.plainTextEdit.setPlainText(str(result))
        con.commit()
        cur.close()

    def back_do(self):
        self.close()
        global ex
        ex.setVisible(True)

    def choise_file(self):
        fname = str(QFileDialog.getOpenFileName()[0])
        self.lineEdit_directory.setText(fname)


class PasswordDel(QDialog):
    def setupUi(self, PasswordDel):
        PasswordDel.setObjectName("PasswordDel")
        PasswordDel.resize(453, 170)
        PasswordDel.setMinimumSize(QtCore.QSize(453, 170))
        PasswordDel.setMaximumSize(QtCore.QSize(453, 170))
        PasswordDel.setStyleSheet("background-color:#c19a6b")
        self.lineEdit_pasword = QtWidgets.QLineEdit(PasswordDel)
        self.lineEdit_pasword.setGeometry(QtCore.QRect(10, 20, 430, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit_pasword.setFont(font)
        self.lineEdit_pasword.setStyleSheet("color: black;\n"
                                            "border:2px solid;\n"
                                            "background-color: rgb(255, 255, 255);")
        self.lineEdit_pasword.setText("")
        self.lineEdit_pasword.setObjectName("lineEdit_pasword")
        self.pushButton_del = QtWidgets.QPushButton(PasswordDel)
        self.pushButton_del.setGeometry(QtCore.QRect(10, 80, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_del.setFont(font)
        self.pushButton_del.setAcceptDrops(True)
        self.pushButton_del.setStyleSheet("QPushButton{\n"
                                              "    color: black;\n"
                                              "    background-color:#b85d43;\n"
                                              "    border-radius:30;\n"
                                              "    border:2px solid\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:pressed{\n"
                                              "    background-color:#6e3727;\n"
                                              "}")
        self.pushButton_del.setObjectName("pushButton_crypted")
        self.pushButton_back = QtWidgets.QPushButton(PasswordDel)
        self.pushButton_back.setGeometry(QtCore.QRect(300, 110, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_back.setFont(font)
        self.pushButton_back.setAcceptDrops(True)
        self.pushButton_back.setStyleSheet("QPushButton{\n"
                                           "    color: black;\n"
                                           "    background-color:#b85d43;\n"
                                           "    border-radius:30;\n"
                                           "    border:2px solid\n"
                                           "}\n"
                                           "\n"
                                           "QPushButton:pressed{\n"
                                           "    background-color:#6e3727;\n"
                                           "}")
        self.pushButton_back.setObjectName("pushButton_back")
        self.label_2 = QtWidgets.QLabel(PasswordDel)
        self.label_2.setPixmap(QPixmap("Imgs/Back.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setGeometry(QtCore.QRect(400, 110, 41, 31))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(PasswordDel)
        self.label.setGeometry(QtCore.QRect(10, 150, 441, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.retranslateUi(PasswordDel)
        QtCore.QMetaObject.connectSlotsByName(PasswordDel)

    def retranslateUi(self, PasswordDel):
        _translate = QtCore.QCoreApplication.translate
        PasswordDel.setWindowTitle(_translate("PasswordDel", "Удаление из базы"))
        self.lineEdit_pasword.setPlaceholderText(_translate("PasswordDel", "Пароль"))
        self.pushButton_del.setText(_translate("PasswordDel", "Удалить из базы"))
        self.pushButton_back.setText(_translate("PasswordDel", "Назад"))
        self.label.setText(_translate("PasswordDel", "После удаления зашифрованый файл будет невозможно расшифровать!"))


class PasswordDelLogic(PasswordDel, QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.file = None

        self.pushButton_back.clicked.connect(self.back_do)
        self.pushButton_del.clicked.connect(self.del_do)

    def back_do(self):  # Возвращение в главное окно
        self.close()
        global ex
        ex.setVisible(True)

    def del_do(self):  # удаление Хэш и salt из бд по паролю
        passwordH = str(md_5(self.lineEdit_pasword.text()))
        sql_delete_query = f"""DELETE FROM Crypt2 WHERE password = '{passwordH}' """
        con = sqlite3.connect("DataBaseP1.db")
        cur = con.cursor()
        try:
            cur.execute(sql_delete_query)
            self.lineEdit_pasword.setText("Данные удалены")
        except Exception:
            self.lineEdit_pasword.setText("Error")
        con.commit()
        cur.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainLogic()
    ex.show()
    sys.exit(app.exec())
