import sys
from collections import Counter
from PyQt5.QtCore import pyqtRemoveInputHook
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction
from PyQt5 import uic
Ui_MainWindow, QtBaseClass = uic.loadUiType('EditorUI.ui')

class MyApp(QMainWindow):
    def __init__(self):
        self.newLines = 1
        super(MyApp, self).__init__(None)
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')

        # New Action
        self.saveAction = QAction('&Save', self)
        self.saveAction.triggered.connect(self.saveCall)
        fileMenu.addAction(self.saveAction)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # New Action
        self.loadAction = QAction('&Load', self)
        self.loadAction.triggered.connect(self.loadCall)
        fileMenu.addAction(self.loadAction)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
    def saveCall(self):
        print('saving')

    def loadCall(self):
        print('loading')

if __name__ == '__main__':
    pyqtRemoveInputHook()
    app = QApplication(sys.argv)
    window = MyApp()
    window.setWindowTitle('Editor')
    window.showMaximized()
    window.show()
    sys.exit(app.exec())
