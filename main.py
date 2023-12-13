import sys

from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox
import re
from layout import Ui_Dialog


class Myform(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()
        self.ui.saveButton.clicked.connect(self.validation)
        self.ui.saveToFileButton.clicked.connect(self.saveToFile)


    def validation(self):
        suma = 0
        wagi = [1,3,7,9,1,3,7,9,1,3,1]
        name = self.ui.nameValue.text()
        secondName = self.ui.secondNameValue.text()
        phoneNumber = self.ui.PhoneValue.text()
        peselNumber = self.ui.peselValue.text()
        if len(name) == 0 or len(secondName) == 0:
            alert = QMessageBox()
            alert.setWindowTitle("Błąd")
            alert.setInformativeText("nieprawidłowy niepoprawne imie lub nazwisko")
            alert.setStandardButtons(QMessageBox.StandardButton.Ok)
            alert.exec()
        if len(phoneNumber) ==9:
            try:
                phoneNumber = int(phoneNumber)
            except:
                alert = QMessageBox()
                alert.setWindowTitle("Błąd")
                alert.setInformativeText("nieprawidłowy numer telefonu")
                alert.setStandardButtons(QMessageBox.StandardButton.Ok)
                alert.exec()
        else:
            alert = QMessageBox()
            alert.setWindowTitle("Błąd")
            alert.setInformativeText("nieprawidłowy numer telefonu")
            alert.setStandardButtons(QMessageBox.StandardButton.Ok)
            alert.exec()
        if len(peselNumber) == 11:
            try:
                int(peselNumber)
            except:
                alert = QMessageBox()
                alert.setWindowTitle("Błąd")
                alert.setInformativeText("nieprawidłowy PESEL")
                alert.setStandardButtons(QMessageBox.StandardButton.Ok)
                alert.exec()


            for i in range(11):
                x = wagi[i]* int(peselNumber[i])
                if x >=10:
                    suma += (x%10)
                else:
                    suma +=x
            if suma % 10 ==0:
                pass
            else:
                alert = QMessageBox()
                alert.setWindowTitle("Błąd")
                alert.setInformativeText("nieprawidłowy PESEL")
                alert.setStandardButtons(QMessageBox.StandardButton.Ok)
                alert.exec()

        else:
            alert = QMessageBox()
            alert.setWindowTitle("Błąd")
            alert.setInformativeText("nieprawidłowy PESEL")
            alert.setStandardButtons(QMessageBox.StandardButton.Ok)
            alert.exec()
    def saveToFile(self):
        name = self.ui.nameValue.text()
        secondName = self.ui.secondNameValue.text()
        data_to_save = name + " "+ secondName
        self.ui.lista.addItem(data_to_save)
        filename = "imie_nazwisko.txt"
        with open(filename,'w') as plik:
            plik.write(data_to_save)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Myform()
    window.show()
    sys.exit(app.exec())