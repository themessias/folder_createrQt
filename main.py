import sys

from folder_creator import *
from lib import *
from PyQt5.QtWidgets import (
    QApplication, QMainWindow
)



class Window(QMainWindow, Ui_MainWindow):
  def __init__(self, parent=None):
    super().__init__(parent)
    self.setupUi(self)
    
    onStart(self.edtCaminho, self.chkPath)
    self.btnProcurar.clicked.connect(lambda: selectFile(self.edtCaminho))
    self.chkPath.stateChanged.connect(lambda: isChecked(self.chkPath,
      self.edtCaminho, self.btnProcurar))
    self.btnCriarPastas.clicked.connect(lambda: runProgram(self.edtCaminho, self.listWidget))
 

if __name__ == "__main__":
  app = QApplication(sys.argv)
  win = Window()
  win.show()
  sys.exit(app.exec())