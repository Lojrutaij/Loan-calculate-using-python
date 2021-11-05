import sys
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

MIN_PRINCIPAL = 10_000.00
MAX_PRINCIPAL = 100_000.00
MIN_RATE = 5.5
MAX_TERM = 7

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self = uic.loadUi('LoanInterface.ui',self)
        self.Interst.setReadOnly(True)
        self.Term.setReadOnly(True)
        self.AmountBorrow.setReadOnly(True)
        self.Interstonloan.setReadOnly(True)
        self.amountloan.setReadOnly(True)
        self.monthlypayment.setReadOnly(True)
        self.calculate.clicked.connect(self.LoanCalculate)


        self.setWindowTitle('Loan Calculate')
        self.setWindowIcon(QtGui.QIcon('Dino1.png'))
        self.show()

    def LoanCalculate(self):
        printcipal = float(self.Loaninput.text())
        interest = float(self.Interestinput.text())
        terms = float(self.Yearsinput.text())

        if printcipal < MIN_PRINCIPAL or printcipal > MAX_PRINCIPAL:
            result = QMessageBox.information(self,'Please Check data','Sorry, the laod is under 10,000 or excess 100,000', QMessageBox.Ok)
            if result == QMessageBox.Ok:
                self.Loaninput.setText('')
            else:
                printcipal = float(self.Loaninput.text())
        
        elif interest < MIN_RATE:
            result = QMessageBox.information(self,'Please Check data','Interest rate less than 5.5', QMessageBox.Ok)
            if result == QMessageBox.Ok:
                self.Interestinput.setText('')
            else:
                interest = float(self.Interestinput.text())
        
        elif terms > MAX_TERM:
            result = QMessageBox.information(self,'Please Check data','Interest rate more than 7', QMessageBox.Ok)
            if result == QMessageBox.Ok:
                self.Yearsinput.setText('')
            else:
                terms = float(self.Yearsinput.text())
        
        else:
            self.AmountBorrow.setText('{:.2f}'.format(printcipal))
            self.Interst.setText('{:.2f}'.format(interest))
            self.Term.setText('{:.0f}'.format(terms))
            Interestloan = printcipal * (interest / 100) * terms
            self.Interstonloan.setText('{:.2f}'.format(Interestloan))
            total = Interestloan + printcipal
            self.amountloan.setText('{:.2f}'.format(total))
            self.monthlypayment.setText('{:.2f}'.format(total / (12 * terms)))


if __name__=='__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())