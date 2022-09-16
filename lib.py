import os

from PyQt5.QtWidgets import QFileDialog, QMessageBox

def getFolder():
  return os.getcwd()

def getFiles(edt):
  files = os.listdir(edt)
  if 'main.py' in files:
    files.remove('main.py')
  files = removeFoldersFromList(files)
  return files

def removeFoldersFromList(list):
  return [element for element in list if "." in element]

def createFolder(path, folderName, listWdgt):
  if not folderExists(path):
    os.mkdir(path)
    listWdgt.addItem(f'Pasta {folderName} criada com sucesso!')

def folderExists(path):
  return os.path.exists(path)

def removeExtension(file):
  return file.rsplit(".")[0]

def moveFile(source, destination, file, listWdgt):
  os.replace(source, destination)
  listWdgt.addItem(f'Arquivo {file} movido com sucesso!')

def isChecked(chkBox, edt, btn):
  if chkBox.isChecked():
    edt.setDisabled(True)
    btn.setDisabled(True)
    edt.setText(getFolder())
  else:
    edt.setDisabled(False)
    btn.setDisabled(False)
          
def selectFile(edt):
  edt.setText(str(QFileDialog.getExistingDirectory()))
  
def onStart(edt, chk):
  if edt.text() == "":
    edt.setText(getFolder())
    chk.setChecked(True)

def runProgram(edt, listWdgt):
  files = getFiles(edt.text())
  for file in files:
    folderName = removeExtension(file)
    path = edt.text() + "\\" + folderName
    createFolder(path, folderName, listWdgt)
    source = edt.text() + "\\" + file
    destination = edt.text() + "\\" + folderName + "\\" + file
    moveFile(source, destination, file, listWdgt)
  msg = QMessageBox()
  msg.setWindowTitle("Sucesso")
  msg.setText("Pastas criadas com sucesso!")
  msg.exec()