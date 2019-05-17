
'''
setAlignment（）对齐
setIndent（）设置缩进
text（）文本内容
setBuddy()设置伙伴关系
setText()设置文本内容
selectedText() 返回当前选择字符
setWordWrap()设置是否允许换行

Qlabel常用信号
鼠标滑过 LinkHovered
单击    LinkActivated

'''
import sys
from PyQt5.QtWidgets import QVBoxLayout,QStatusBar,QToolTip,QLabel,QMainWindow,QApplication,QPushButton,QWidget
from PyQt5.QtGui import QPalette,QPixmap
from PyQt5.QtCore import Qt

class QlabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def  initUi(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText("<font color=yellow>这是一个文本标签.</font>")
        label1.setAutoFillBackground(True)
        palette = QPalette()
        palette.setColor(QPalette.Window,Qt.blue)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'>欢迎使用Python GUI程序</a>")

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('这是一个图片标签')
        label3.setPixmap(QPixmap("./images/python.jpg"))


        label4.setText("<a href='http://www.baidu.com'>谢谢关注</a>")

        label4.setOpenExternalLinks(True)
        # false是响应函数，true是打开外部链接
        label4.setToolTip('这是一个超链接')
        label4.setAlignment(Qt.AlignRight)

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        self.setLayout(vbox)
        self.setWindowTitle('QLabel')
        # self.status = self.statusBar()

        label2.linkHovered.connect(self.linkhovered)
        label4.linkActivated.connect(self.linkclicked)

    def linkhovered(self):
        print('鼠标滑过label2')
        # self.status.showMessage('鼠标滑过label2')

    def linkclicked(self):
        print('鼠标点击label4')
        # self.status.showMessage('鼠标点击label4')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    lab = QlabelDemo()
    lab.show()

    sys.exit(app.exec_())
