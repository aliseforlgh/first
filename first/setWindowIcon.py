import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtGui import QIcon

class IconForm(QMainWindow):
    def __init__(self):
        super(IconForm, self).__init__()
        self.Ui_init()

    def Ui_init(self):
        self.setGeometry(500,500,400,400)
        self.setWindowTitle('设置窗口的icon')

        self.setWindowIcon(QIcon('./images/phoenix.ico'))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon('./image/logo.ico'))
    ico = IconForm() 
    ico.show()

    sys.exit(app.exec_())
