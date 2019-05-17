import sys
from PyQt5.QtWidgets import QHBoxLayout,QDesktopWidget,QToolTip,QMainWindow,QApplication,QPushButton,QWidget
from PyQt5.QtGui import QFont


class TooltipForm(QMainWindow):
    def __init__(self):
        super(TooltipForm, self).__init__()
        self.Ui_init()

    def Ui_init(self):
        QToolTip.setFont(QFont('SansSerif',12))
        self.setToolTip('今天<b>是星期六</b>')
        self.setGeometry(500,500,300,300)

        self.setWindowTitle('1551')

        self.button1 = QPushButton('我的按钮')
        self.button1.setToolTip('z这只是一个按钮')

        layout1 = QHBoxLayout()
        layout1.addWidget(self.button1)

        mainFrame = QWidget()
        mainFrame.setLayout(layout1)

        self.setCentralWidget(mainFrame)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    tool = TooltipForm()
    tool.show()

    sys.exit(app.exec_())

