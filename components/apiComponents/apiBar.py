from PyQt5.QtWidgets import (QHBoxLayout, QLineEdit, QWidget, QComboBox)

class ApiBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.apiMethod = QComboBox()
        self.apiUrl = QLineEdit()
        self.apiMethodText = ""
        self.apiUrlText = ""
        self.initUi()

    def initUi(self):
        # initialize the API method
        self.apiMethod.addItems(["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS", "HEAD"])

        # initialize the API URL input
        self.apiUrl.setPlaceholderText("API Endpoint")

        self.setLayout(QHBoxLayout())
        self.layout().addWidget(self.apiMethod, 2)
        self.layout().addWidget(self.apiUrl, 8)

    def getData(self):
        self.apiMethodText = self.apiMethod.currentText()
        self.apiUrlText = self.apiUrl.text()
        return self.apiMethodText, self.apiUrlText
