import utils, pyqt
from PyQt5.QtWidgets import QApplication
import sys
import pyqt

if __name__ == "__main__":
    app = QApplication([])
    if not utils.get_info("path"):
        main_widget = pyqt.Creds()
    if not utils.get_info("user"):
        main_widget = pyqt.Login()
    else : 
        main_widget = pyqt.Chat()
    main_widget.show()
    app.exec_()
