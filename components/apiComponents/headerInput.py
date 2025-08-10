from PyQt5.QtWidgets import QCheckBox, QHBoxLayout, QLineEdit, QWidget


class HeaderInput(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.checkBox = QCheckBox(self)
        self.keyInput = QLineEdit(self)
        self.valueInput = QLineEdit(self)
        self.initUi()

    def initUi(self):
        self.setLayout(QHBoxLayout())
        self.keyInput.setPlaceholderText("Key")
        self.valueInput.setPlaceholderText("Value")
        self.layout().addWidget(self.checkBox, 1)
        self.layout().addWidget(self.keyInput, 3)
        self.layout().addWidget(self.valueInput, 6)

    def getHeaderData(self):
        key = self.keyInput.text().strip()
        value = self.valueInput.text().strip()
        return key, value