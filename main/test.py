from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QLineEdit, QTextEdit, QHBoxLayout
import json
import utils
from firebase_admin import db

class creds(QWidget):
    """This is the widget to specify our credentials location/path"""
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self) :
        layout = QVBoxLayout()
        
        return