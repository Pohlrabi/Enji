import utils, pyqt
from PyQt5.QtWidgets import QApplication
import sys
import pyqt

ref = utils.initialize()

if __name__ == "__main__":
    app = QApplication([])
    main_widget = pyqt.MainWidget(ref)
    main_widget.show()
    app.exec_()
