from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLineEdit, QTextEdit
from PyQt5.QtCore import Qt
import json

class PayloadInput(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.data = ""
        self.mainWindow = QWidget(self)
        self.payloadDataInput = QTextEdit(self)
        self.prettifyButton = QPushButton("Prettify", self)
        self.initUI()

    def initUI(self):
        # Set up the user interface
        self.setWindowTitle("Payload Input")
        self.setGeometry(100, 100, 400, 300)

        # Set up the main window layout
        self.mainLayout = QVBoxLayout(self.mainWindow)
        self.mainWindow.setLayout(self.mainLayout)

        # Add the button to the main window
        self.payloadDataInput.setPlaceholderText("Enter your payload here...")
        self.payloadDataInput.setAlignment(Qt.AlignLeft| Qt.AlignTop)
        self.payloadDataInput.setMinimumWidth(300)
        self.payloadDataInput.setMinimumHeight(150)
        self.mainLayout.addWidget(self.payloadDataInput, 9)
        self.mainLayout.addWidget(self.prettifyButton, 1)

        self.prettifyButton.clicked.connect(self.prettifyPayload)

    def getPayloadData(self):
        return self.payloadDataInput.toPlainText()
    
    def prettifyPayload(self):
        # Placeholder for prettifying logic
        payload = self.getPayloadData()
        if payload:
            # Here you would implement the actual prettifying logic
            try:
                json_data = json.loads(payload)
                self.data = json.dumps(json_data, indent=4)
                print(self.data)
            except json.JSONDecodeError:
                self.data = payload
                print("Invalid JSON format, returning original payload.")
        self.payloadDataInput.setPlainText(self.data)
