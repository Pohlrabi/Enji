from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QLineEdit, QTextEdit, QHBoxLayout
import json
import utils
from firebase_admin import db


class Creds(QWidget):
    def __init__(self):
        super().__init__()

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

        self.setWindowTitle("Credential")

    def select_path(self):
        # Show a file or directory selection dialog
        path, _ = QFileDialog.getOpenFileName()
        try :
            with open("creds.json","w") as f:
                path = {"path":path}
                json.dump(path,f)
        except :
            print("Error!")

class Login(QWidget):
    def __init__(self):
        super().__init__()

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

    def name_submit(self):
        print(self.name_edit.text())
        try:
            with open("user.json", "w") as f:
                user = {"user":self.name_edit.text()}
                json.dump(user,f)
        except:
            print("name error?")


class Chat(QWidget):
    def __init__(self, ref):
        super().__init__()
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
        try:
            for key, data in self.room_data.items():
                self.scroll_area.append(data["user"] + " : " + data["message"] + "\n")
        except:
            self.scroll_area.append(self.room_data["user"] + " : " + self.room_data["message"] + "\n")
    def on_enter(self):
        # When the input field's return key is pressed, get the text from the input field and append it to the text edit
        input_text = self.input_field.text()
        data, room = utils.set_data(user=utils.get_user(), msg=input_text)
        utils.send_msg(self.ref,data,room)
        self.input_field.clear()

    def on_click(self):
        # When the button is clicked, get the text from the input field and append it to the text edit
        input_text = self.input_field.text()
        data, room = utils.set_data(user=utils.get_user(), msg=input_text)
        utils.send_msg(self.ref,data,room)
        self.input_field.clear()

class MainWidget(QWidget):
    def __init__(self, ref):
        super().__init__()
        self.ref = ref
        # Set up the layout for the main widget
        self.layout = QVBoxLayout(self)
        # Create the widgets and add them to the layout

        try:
            with open("creds.json", "r") as f:
                with open("user.json", "r") as k: 
                    if ("user" in json.load(k)) :
                        print("hey")
                        self.widget3 = Chat(self.ref)
                        print("hey again")
                        self.switch_widgets3()
                        print("wtf")
                    elif ("path" in json.load(f)) :
                        self.widget2 = Login()
                        self.widget3 = Chat(self.ref)
                        self.switch_widgets2()
        except:
            self.widget1 = Creds()
            self.widget2 = Login()
            self.widget3 = Chat(self.ref)
            self.layout.addWidget(self.widget1)


        # Connect the "clicked" signal of the buttons to the switch_widgets slot
        try :
            self.widget1.confirm.clicked.connect(self.switch_widgets2)
            self.widget2.submit_button.clicked.connect(self.switch_widgets3)
        except:
            pass

    def switch_widgets2(self):
        # Remove the current widget from the layout
        current_widget = self.layout.takeAt(0).widget()
        current_widget.setParent(None)

        self.layout.addWidget(self.widget2)
        self.setGeometry(300, 300, 340, 150)
        self.setWindowTitle("Login")
    
    def switch_widgets3(self):
        # Remove the current widget from the layout
        try:
            current_widget = self.layout.takeAt(0).widget()
            current_widget.setParent(None)
        except:
            pass
        self.layout.addWidget(self.widget3)
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle("Chat")


if __name__ == "__main__":
    app = QApplication([])
    main_widget = MainWidget()
    main_widget.show()
    app.exec_()
