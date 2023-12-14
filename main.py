import sys

from PyQt6.QtWidgets import QApplication, QDialog, QMessageBox
import re
from layout import Ui_Dialog



class Myform(QDialog):
    isValid = True
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()
        self.ui.saveButton.clicked.connect(self.saveToComboBox)
        self.ui.saveToFileButton.clicked.connect(self.saveToFile)
    def allert(self):
        self.isValid = False
        alert = QMessageBox()
        alert.setWindowTitle("Błąd")
        alert.setInformativeText("Nieprawidłowe dane spróbój ponownie")
        alert.setStandardButtons(QMessageBox.StandardButton.Ok)
        alert.exec()

    def validation(self):
        suma = 0
        wagi = [1,3,7,9,1,3,7,9,1,3,1]
        name = self.ui.nameValue.text()
        secondName = self.ui.secondNameValue.text()
        phoneNumber = self.ui.PhoneValue.text()
        peselNumber = self.ui.peselValue.text()
        if len(name) == 0 or len(secondName) == 0:
            self.allert()
        if len(phoneNumber) ==9:
            try:
                phoneNumber = int(phoneNumber)
                self.isValid = True
            except:
                self.allert()
        else:
            self.allert()
        if len(peselNumber) == 11:
            try:
                int(peselNumber)
                self.isValid = True
            except:
                self.allert()


            for i in range(11):
                x = wagi[i]* int(peselNumber[i])
                if x >=10:
                    suma += (x%10)
                else:
                    suma +=x
            if suma % 10 ==0:
                pass
            else:
                self.allert()

        else:
            self.allert()
    def saveToFile(self):
        self.validation()
        if self.isValid == True:
            name = self.ui.nameValue.text()
            secondName = self.ui.secondNameValue.text()
            phoneNumber = self.ui.PhoneValue.text()
            peselNumber = self.ui.peselValue.text()
            checkBoxValue = self.ui.typeCheckBox.isChecked()
            if checkBoxValue == True:
                data_to_save = f"Imie: {name}\nNazwisko: {secondName}\nNumer telefonu: {phoneNumber}\nPESEL: {peselNumber}\nCzy Umowa o prace: TAK\n"
            else:
                data_to_save = f"Imie: {name}\nNazwisko: {secondName}\nNumer telefonu: {phoneNumber}\nPESEL: {peselNumber}\nCzy Umowa o prace: NIE\n"
            filename = "imie_nazwisko.txt"
            with open(filename,'a') as plik:
                plik.write(data_to_save)
    def saveToComboBox(self):
        self.validation()
        if self.isValid == True:
            name = self.ui.nameValue.text()
            secondName = self.ui.secondNameValue.text()
            data_to_save = f"{name} {secondName}"
            self.ui.lista.addItem(data_to_save)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Myform()
    window.show()
    sys.exit(app.exec())