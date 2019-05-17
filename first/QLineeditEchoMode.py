import sys
from PyQt5.QtWidgets import *


class Qlineeditecho(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle('echo mode')
        normaledit = QLineEdit()
        noechoedit = QLineEdit()
        passwordedit = QLineEdit()
        passwordechoedit = QLineEdit()

        formlayout = QFormLayout()
        formlayout.addRow('Normal',normaledit)
        formlayout.addRow('Noecho',noechoedit)
        formlayout.addRow('Password',passwordedit)
        formlayout.addRow('Passwordecho',passwordechoedit)

        self.setLayout(formlayout)
#         placeholdertext

        normaledit.setEchoMode(QLineEdit.Normal)
        noechoedit.setEchoMode(QLineEdit.NoEcho)
        passwordedit.setEchoMode(QLineEdit.Password)
        passwordechoedit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        normaledit.setPlaceholderText('Normal')
        noechoedit.setPlaceholderText('Noecho')
        passwordedit.setPlaceholderText('Password')
        passwordechoedit.setPlaceholderText('Passwordecho')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    lineecho = Qlineeditecho()
    lineecho.show()

    sys.exit(app.exec_())
