from PyQt5.QtWidgets import (QWidget, QVBoxLayout)
from PyQt5.QtCore import Qt
from components.apiComponents.headerInput import HeaderInput

class HeaderList(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.headerNumber = 2
        self.setLayout(QVBoxLayout())
        self.layout().setAlignment(Qt.AlignTop)

        # Placeholder for header inputs
        self.headerInputs = []
        for _ in range(self.headerNumber):
            self.addHeaderInput()

    def addHeaderInput(self):
        header_input = HeaderInput(self)
        self.headerInputs.append(header_input)
        self.layout().addWidget(header_input)  # Add the new header input to the layout
        self.update()

    def getHeadersList(self):
        headers = []
        for header_input in self.headerInputs:
            key, value = header_input.getHeaderData()
            if key and value:
                headers.append((key, value))
        return headers