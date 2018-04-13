import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Files'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.nomFichier=""
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.openFolderNamesDialog()
        self.show()

    def openFolderNamesDialog(self):
        #options = QFileDialog.Options()
        #options |= QFileDialog.DirectoryOnly
        #options |= QFileDialog.DontUseNativeDialog
        #fileName, _ = QFileDialog.getOpenFileName(self,"Open files", "","All Files (*);;Python Files (*.py);;File", options=options)
        #if fileName:
        #    print(fileName)
        #    self.nomFichier=fileObj
        #QStringdir = QFileDialog.getExistingDirectory(self, tr("Open Directory"), "/home", QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks);
        folderName = QFileDialog.getExistingDirectory(self,
                     "Ouverture projet",
                     ".",
                     QFileDialog.ShowDirsOnly)
        if folderName:
            print(folderName)
            self.nomFichier=folderName
