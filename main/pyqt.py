from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QLineEdit, QTextEdit, QHBoxLayout
import json
import utils
from firebase_admin import db


class Creds(QWidget):
    def __init__(self):
        super().__init__()

        self.w = None

        # Set up the layout and add a button
        self.layout = QVBoxLayout(self)
        self.button = QPushButton("Select a file or directory")
        self.button.move(20, 20)
        self.button.resize(280, 30)
        self.layout.addWidget(self.button)

        # Connect the "clicked" signal of the button to the select_path slot
        self.button.clicked.connect(self.select_path)

        # Add confirm button
        self.confirm = QPushButton("Confirm")
        self.layout.addWidget(self.confirm)
        self.confirm.clicked.connect(self.confirms)
        self.setWindowTitle("Credential")

    def select_path(self):
        # Show a file or directory selection dialog
        path, _ = QFileDialog.getOpenFileName()
        utils.write_info("path", path)
    
    def confirms(self):
        self.w = Login()
        self.w.show()
        self.close()

class Login(QWidget):
    def __init__(self):
        super().__init__()

        self.w = None

        # Create a label to prompt the user to enter their name
        self.layout = QVBoxLayout()
        self.name_label = QLabel("Enter your name:", self)
        self.name_label.move(20, 20)
        self.layout.addWidget(self.name_label)

        # Create a line edit widget to allow the user to enter their name
        self.name_edit = QLineEdit(self)
        self.name_edit.move(20, 50)
        self.name_edit.resize(280, 30)
        self.layout.addWidget(self.name_edit)

        # Create a submit button
        self.submit_button = QPushButton("Submit", self)
        self.submit_button.move(20, 90)
        self.submit_button.resize(280, 30)
        self.layout.addWidget(self.submit_button)
        self.submit_button.clicked.connect(self.name_submit)
        self.submit_button.clicked.connect(self.confirms)

    def name_submit(self):
        utils.write_info("user", self.name_edit.text())

    def confirms(self):
        self.w = Chat()
        self.w.show()
        self.close()


class Chat(QWidget):
    def __init__(self):
        super().__init__()
        ref = utils.initialize()
        self.ref = ref
        # Create a vertical layout to hold the scroll area, input field, and button
        self.layout = QVBoxLayout(self)
        
        # Create the scroll area and set its widget to be a text edit
        self.scroll_area = QTextEdit()
        self.scroll_area.setReadOnly(True)
        self.layout.addWidget(self.scroll_area)

        # Create a horizontal layout to hold the input field and button
        input_layout = QHBoxLayout()

        # Create the input field and connect its returnPressed signal to the on_enter method
        self.input_field = QLineEdit()
        self.input_field.returnPressed.connect(self.on_enter)
        input_layout.addWidget(self.input_field)

        # Create the submit button and connect its clicked signal to the on_click method
        self.submit_button = QPushButton('Submit')
        self.submit_button.clicked.connect(self.on_click)
        input_layout.addWidget(self.submit_button)

        # Add the input layout to the main layout
        self.layout.addLayout(input_layout)

        # Add listener
        db.reference("/chat").child("2").listen(self.listener)
    def listener(self,event):
        print(event.data)
        self.room_data = event.data
        if event.data == None :
            return
        try:
            for key, data in self.room_data.items():
                self.scroll_area.append(data["user"] + " : " + data["message"] + "\n")
        except:
            self.scroll_area.append(self.room_data["user"] + " : " + self.room_data["message"] + "\n")
    def on_enter(self):
        # When the input field's return key is pressed, get the text from the input field and append it to the text edit
        input_text = self.input_field.text()
        data, room = utils.set_data(user=utils.get_info("user"), msg=input_text)
        utils.send_msg(self.ref,data,room)
        self.input_field.clear()

    def on_click(self):
        # When the button is clicked, get the text from the input field and append it to the text edit
        input_text = self.input_field.text()
        data, room = utils.set_data(user=utils.get_info("user"), msg=input_text)
        utils.send_msg(self.ref,data,room)
        self.input_field.clear()

if __name__ == "__main__":
    app = QApplication([])
    if not utils.get_info("path"):
        main_widget = Creds()
    if not utils.get_info("user"):
        main_widget = Login()
    else : 
        main_widget = Chat()
    main_widget.show()
    app.exec_()
