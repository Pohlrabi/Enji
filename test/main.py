import utils, pyqt
from PyQt5.QtWidgets import QApplication
import sys
import pyqt

ref = utils.initialize()

data, room = utils.set_data(user="Pohl", msg="hello", room = "2")
utils.send_msg(ref,data, room)

label = ref.get()
label = label.keys()
print(label)


if __name__ == "__main__":
    app = QApplication([])
    main_widget = pyqt.MainWidget()
    main_widget.show()
    app.exec_()
