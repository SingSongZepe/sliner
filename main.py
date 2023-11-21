import sys

from sline import SLINE

from PySide6.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    sl = SLINE()
    sl.show()
    app.exec()
