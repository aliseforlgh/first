import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Combox(QWidget):
    def __init__(self):
        super(Combox, self).__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle('combox测试')
        self.resize(300,100)

        self.label = QLabel('请选择编程语言')
        self.comb = QComboBox()
        self.comb.addItem('1')
        self.comb.addItem('2')
        self.comb.addItem('3')
        self.comb.addItem('4')
        self.comb.addItem('5')
        self.comb.addItem('6')
        self.comb.addItem('7')
        self.comb.addItem('8')
        layout1 = QVBoxLayout()
        layout1.addWidget(self.label)
        layout1.addWidget(self.comb)
        self.setLayout(layout1)
        self.comb.currentIndexChanged.connect(self.comboxchange)

    def comboxchange(self,i):
        self.label.setText(self.comb.currentText())
        self.label.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Combox()
    main.show()

    sys.exit(app.exec_())
