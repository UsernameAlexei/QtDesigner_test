# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc4.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(369, 490)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(0, 0, 371, 91))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_result.setFont(font)
        self.label_result.setStyleSheet("background-color: rgb(225, 225, 225);")
        self.label_result.setObjectName("label_result")
        self.Button_0 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_0.setGeometry(QtCore.QRect(0, 410, 140, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Button_0.setFont(font)
        self.Button_0.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.Button_0.setObjectName("Button_0")
        self.Button_equal = QtWidgets.QPushButton(self.centralwidget)
        self.Button_equal.setGeometry(QtCore.QRect(280, 410, 90, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Button_equal.setFont(font)
        self.Button_equal.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.Button_equal.setObjectName("Button_equal")
        self.Button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_2.setGeometry(QtCore.QRect(0, 330, 140, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Button_2.setFont(font)
        self.Button_2.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.Button_2.setObjectName("Button_2")
        self.Button_4 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_4.setGeometry(QtCore.QRect(0, 250, 140, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Button_4.setFont(font)
        self.Button_4.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.Button_4.setObjectName("Button_4")
        self.Button_6 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_6.setGeometry(QtCore.QRect(0, 170, 140, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Button_6.setFont(font)
        self.Button_6.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.Button_6.setObjectName("Button_6")
        self.Button_8 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_8.setGeometry(QtCore.QRect(0, 90, 140, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Button_8.setFont(font)
        self.Button_8.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.Button_8.setObjectName("Button_8")
        self.Button_1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_1.setGeometry(QtCore.QRect(140, 410, 140, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Button_1.setFont(font)
        self.Button_1.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.Button_1.setObjectName("Button_1")
        self.Button_3 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_3.setGeometry(QtCore.QRect(140, 330, 140, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Button_3.setFont(font)
        self.Button_3.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.Button_3.setObjectName("Button_3")
        self.Button_5 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_5.setGeometry(QtCore.QRect(140, 250, 140, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Button_5.setFont(font)
        self.Button_5.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.Button_5.setObjectName("Button_5")
        self.Button_7 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_7.setGeometry(QtCore.QRect(140, 170, 140, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Button_7.setFont(font)
        self.Button_7.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.Button_7.setObjectName("Button_7")
        self.Button_9 = QtWidgets.QPushButton(self.centralwidget)
        self.Button_9.setGeometry(QtCore.QRect(140, 90, 140, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Button_9.setFont(font)
        self.Button_9.setStyleSheet("background-color: rgb(255, 170, 127);")
        self.Button_9.setObjectName("Button_9")
        self.Button_plus = QtWidgets.QPushButton(self.centralwidget)
        self.Button_plus.setGeometry(QtCore.QRect(280, 330, 90, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Button_plus.setFont(font)
        self.Button_plus.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.Button_plus.setObjectName("Button_plus")
        self.Button_minus = QtWidgets.QPushButton(self.centralwidget)
        self.Button_minus.setGeometry(QtCore.QRect(280, 250, 90, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Button_minus.setFont(font)
        self.Button_minus.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.Button_minus.setObjectName("Button_minus")
        self.Button_mult = QtWidgets.QPushButton(self.centralwidget)
        self.Button_mult.setGeometry(QtCore.QRect(280, 170, 90, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Button_mult.setFont(font)
        self.Button_mult.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.Button_mult.setObjectName("Button_mult")
        self.Button_sep = QtWidgets.QPushButton(self.centralwidget)
        self.Button_sep.setGeometry(QtCore.QRect(280, 90, 90, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Button_sep.setFont(font)
        self.Button_sep.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.Button_sep.setObjectName("Button_sep")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()
        self.is_equal = False

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
        self.label_result.setText(_translate("MainWindow", "0"))
        self.Button_0.setText(_translate("MainWindow", "0"))
        self.Button_equal.setText(_translate("MainWindow", "="))
        self.Button_2.setText(_translate("MainWindow", "2"))
        self.Button_4.setText(_translate("MainWindow", "4"))
        self.Button_6.setText(_translate("MainWindow", "6"))
        self.Button_8.setText(_translate("MainWindow", "8"))
        self.Button_1.setText(_translate("MainWindow", "1"))
        self.Button_3.setText(_translate("MainWindow", "3"))
        self.Button_5.setText(_translate("MainWindow", "5"))
        self.Button_7.setText(_translate("MainWindow", "7"))
        self.Button_9.setText(_translate("MainWindow", "9"))
        self.Button_plus.setText(_translate("MainWindow", "+"))
        self.Button_minus.setText(_translate("MainWindow", "-"))
        self.Button_mult.setText(_translate("MainWindow", "*"))
        self.Button_sep.setText(_translate("MainWindow", "/"))

    def add_functions(self):
        self.Button_0.clicked.connect(lambda: self.write_number(self.Button_0.text()))
        self.Button_1.clicked.connect(lambda: self.write_number(self.Button_1.text()))
        self.Button_2.clicked.connect(lambda: self.write_number(self.Button_2.text()))
        self.Button_3.clicked.connect(lambda: self.write_number(self.Button_3.text()))
        self.Button_4.clicked.connect(lambda: self.write_number(self.Button_4.text()))
        self.Button_5.clicked.connect(lambda: self.write_number(self.Button_5.text()))
        self.Button_6.clicked.connect(lambda: self.write_number(self.Button_6.text()))
        self.Button_7.clicked.connect(lambda: self.write_number(self.Button_7.text()))
        self.Button_8.clicked.connect(lambda: self.write_number(self.Button_8.text()))
        self.Button_9.clicked.connect(lambda: self.write_number(self.Button_9.text()))

        self.Button_plus.clicked.connect(lambda: self.write_number(self.Button_plus.text()))
        self.Button_minus.clicked.connect(lambda: self.write_number(self.Button_minus.text()))
        self.Button_mult.clicked.connect(lambda: self.write_number(self.Button_mult.text()))
        self.Button_sep.clicked.connect(lambda: self.write_number(self.Button_sep.text()))

        self.Button_equal.clicked.connect(self.results)

    def write_number(self, number):
        if self.label_result.text() == "0" or self.is_equal:
            self.label_result.setText(number)
            self.is_equal = False
        else:
            self.label_result.setText(self.label_result.text() + number)

    def results(self):
        if not self.is_equal:
            res = eval(self.label_result.text())
            self.label_result.setText("Результат: " + str(res))
            self.is_equal = True
        else:
            # всплывающие окна
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Сейчас это действие выполнить нельзя")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Reset | QMessageBox.Cancel | QMessageBox.Ok)

            error.setDefaultButton(QMessageBox.Ok)
            error.setInformativeText("Действие не выполнить")
            error.setDetailedText('Описание')

            error.buttonClicked.connect(self.popup_action)

            error.exec_()

    def popup_action(self, btn):
        if btn.text() == 'Ok':
            print('print ok')
        elif btn.text() == "Reset":
            self.label_result.setText("")
            self.is_equal = False


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
