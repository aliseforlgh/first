import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QPushButton,QHBoxLayout

class germory(QMainWindow):
    def __init__(self):
        super(germory, self).__init__()
        self.setWindowTitle('拖拽显示坐标')
        self.resize(600,500)
        self.move(600,500)
        self.button = QPushButton('click')


        self.button.resize(200,100)
        self.button.clicked.connect(self.btn_drap)

        # self.button.move.connect(self.btn_drap)
        self.statu = self.statusBar()

        self.statu.showMessage('login')

        layout = QHBoxLayout()
        layout.addWidget(self.button)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)


    def btn_drap(self):
        self.statu.showMessage('width: %d ,height: %d ,x: %d ,y: %d ' % (self.window().width(),self.window().height(),self.window().x(),self.window().y()))
        # print('%d,%d,%d,%d' % (self.window().width(),self.window().height(),self.window().x(),self.window().y()))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ge = germory()
    ge.show()

    sys.exit(app.exec_())

