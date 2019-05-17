# QDesktopWidget
import sys
# from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow,QDesktopWidget,QHBoxLayout,QPushButton
# from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QHBoxLayout,QDesktopWidget,QMainWindow,QApplication,QPushButton,QWidget


class CenterForm(QMainWindow):
    def __init__(self):
        super(CenterForm, self).__init__()
        self.setWindowTitle('退出应用程序')
        self.resize(300,120)
        # self.status = self.statusBar()
        # self.status.showMessage('五秒钟的记忆',5000)
        # self.center()
        # 添加button
        self.button = QPushButton('退出应用程序')
        # self.button.move(200,200)
        self.button.clicked.connect(self.onClickButton)

        layout = QHBoxLayout()
        layout.addWidget(self.button)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

    def onClickButton(self):
        sender = self.sender()
        print(sender.text() + ' 按钮被按下')
        # sender = self.sender()
        # print(sender.text() +'按钮被按下')
        app = QApplication.instance()
        app.quit()


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

