import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class FirstMainWindow(QMainWindow):
    def __init__(self):
        super(FirstMainWindow, self).__init__()

        self.resize(400,300)

        self.status = self.statusBar()
        self.status.showMessage('五秒钟的记忆',5000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = FirstMainWindow()
    w.setWindowTitle('我的第一个窗口')

    w.show()

    sys.exit(app.exec_())
