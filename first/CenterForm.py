# QDesktopWidget
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QDesktopWidget
# from PyQt5.QtGui import QIcon


class CenterForm(QMainWindow):
    def __init__(self):
        super(CenterForm, self).__init__()

        self.setWindowTitle('窗口居中')

        self.resize(800,600)

        self.status = self.statusBar()
        self.status.showMessage('五秒钟的记忆',5000)
        self.center()

    def center(self):
        screen = QDesktopWidget() .screenGeometry()
        size = self.geometry()

        new_left = (screen.width() - size.width())/2
        new_top = (screen.height() - self.height())/2
        self.move(new_left,new_top)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    center = CenterForm()
    center.show()

    sys.exit(app.exec_())

