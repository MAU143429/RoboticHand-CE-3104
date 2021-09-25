# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditorUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QFileDialog
from Hardware.Robotic_Hand.Translator import Translator
from Hardware.Robotic_Hand.Translator import Execute
from Software.GUI.codeeditor import CodeEditor
from Software.Lexical_Analysis.myLexer import *
from threading import *
import os
import time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1500, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.codeEditor = CodeEditor(self.centralwidget)
        self.codeEditor.setGeometry(QtCore.QRect(0, 0, 1369, 550))
        self.codeEditor.setStyleSheet("background-color: rgb(33, 33, 50);\n"
                                      "font: 75 15pt \"Consolas\";\n"
                                      "color: rgb(255, 255, 255);")
        self.codeEditor.setPlainText("")
        self.codeEditor.setObjectName("codeEditor")
        self.output = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(0, 550, 1369, 250))
        self.output.setReadOnly(True)
        self.output.setObjectName("output")
        self.compileButton = QtWidgets.QPushButton(self.centralwidget)
        self.compileButton.setGeometry(QtCore.QRect(1369, 0, 131, 400))
        self.compileButton.setObjectName("compileButton")
        self.runButton = QtWidgets.QPushButton(self.centralwidget)
        self.runButton.setGeometry(QtCore.QRect(1369, 400, 131, 400))
        self.runButton.setObjectName("runButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 801, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menuBar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.setShortcut('Ctrl+S')
        self.actionSave.triggered.connect(self.save)
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionLoad.setShortcut('Ctrl+L')
        self.actionLoad.triggered.connect(self.load)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionLoad)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.compileButton.clicked.connect(self.start_compile)
        self.runButton.clicked.connect(self.start_run_compile)
        self.menuFile
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.output.setPlainText(_translate("MainWindow", ">>>\n"
                                                          ""))
        self.compileButton.setText(_translate("MainWindow", "Compile"))
        self.runButton.setText(_translate("MainWindow", "Compile and Run"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))

    def save(self):
        with open('../Lexical_Analysis/source.txt', 'w') as f:
            code = self.codeEditor.toPlainText()
            f.write(code)
            f.close()

    def load(self):
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        with open(path, "r") as f:
            self.codeEditor.setPlainText(f.read())
            f.close()

    def compile(self):
        self.save()
        time.sleep(1)
        t = Translator()
        t.Clean()
        error = ErrorLog()
        error.clean()
        myTable.Clean()
        lex_test()
        if error.log != "":
            print(" \n ERRORES DE COMPILACION \n")
            error.print()
            self.output.setPlainText(error.print())
        else:
            print("NO HAY ERRORES")

    def run_compile(self):
        self.save()
        #self.output.setPlainText(self.codeEditor.toPlainText())
        time.sleep(1)
        t = Translator()
        t.Clean()
        error = ErrorLog()
        error.clean()
        myTable.Clean()
        lex_test()
        t.Write("1")
        print("VOY A EJECUTAR EL CODIGO")
        if error.log != "":
            error.print()
        else:
            print("VOY A ENVIAR LOS ARCHIVOS LA MANO")
            time.sleep(1)
            e = Execute()
            e.execute()
            print("ARCHIVOS ENVIADOS")

    def start_compile(self):


        thread = Thread(target=self.compile(), args=())
        thread.start()
        thread.join()
        print("HILOS ACTIVOS")



    def start_run_compile(self):

        thread1 = Thread(target=self.run_compile(), args=())
        thread1.start()
        thread1.join()
        print("HILOS ACTIVOS")



if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
