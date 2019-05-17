import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QRegExpValidator
from PyQt5.QtCore import QRegExp
# 校验器

class Validator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle('校验器')
        formlayout = QFormLayout()

        intLineedit = QLineEdit()
        doublelineedit = QLineEdit()
        validatoredit = QLineEdit()

        # intLineedit.setInputMask()

        formlayout.addRow('整数',intLineedit)
        formlayout.addRow('浮点',doublelineedit)
        formlayout.addRow('正则',validatoredit)

        intLineedit.setPlaceholderText('int')
        doublelineedit.setPlaceholderText('double')
        validatoredit.setPlaceholderText('validator')

        # 整数校验器
        intvalidator = QIntValidator(self)
        intvalidator.setRange(-99999,99999)

        # double浮点校验
        doublevalidator = QDoubleValidator(self)
        # doublevalidator.setRange(-360,360,2)
        doublevalidator.setRange(-360,360)
        doublevalidator.setNotation(QDoubleValidator.StandardNotation)
        doublevalidator.setDecimals(2)

        # 正则校验
        reg =QRegExp('[a-zA-Z0-9]+$')
        validator = QRegExpValidator(self)
        validator.setRegExp(reg)

#         设置校验器
        intLineedit.setValidator(intvalidator)
        doublelineedit.setValidator(doublevalidator)
        validatoredit.setValidator(validator)
        self.setLayout(formlayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    vali = Validator()
    vali.show()
    sys.exit(app.exec_())




