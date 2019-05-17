import sys
from PyQt5.QtWidgets import QDialog,QGridLayout,QLineEdit,QToolTip,QLabel,QMainWindow,QApplication,QPushButton,QWidget
from PyQt5.QtGui import QPalette,QPixmap
from PyQt5.QtCore import Qt


class QLabelBuddy(QDialog):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle('设置伙伴关系')
        namelabel1 = QLabel('&Name',self)

        nameedit1 = QLineEdit(self)

        # namelabel1.setBuddy(nameedit1)

        namelabel2 = QLabel('&Pass',self)
        nameedit2 = QLineEdit(self)
        namelabel2.setBuddy(nameedit2)

        btnOK = QPushButton('&OK')
        btnCancel = QPushButton('&Cancel')

        layout1 = QGridLayout()

        layout1.addWidget(namelabel1,0,0)
        layout1.addWidget(nameedit1,0,1,1,2)

        layout1.addWidget(namelabel2,1,0)
        layout1.addWidget(nameedit2,1,1,1,2)
        layout1.addWidget(btnOK,2,1)
        layout1.addWidget(btnCancel,2,2)



        self.setLayout(layout1)




if __name__ == '__main__':
    app = QApplication(sys.argv)

    qlabel = QLabelBuddy()
    qlabel.show()
    sys.exit(app.exec_())

