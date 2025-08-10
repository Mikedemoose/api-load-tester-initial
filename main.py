import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtCore import Qt
from components.addAPI import AddAPIWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ItemList = []
        self.Counter = 0
        self.CurrentItemName = ""
        self.saveWorkflowButton = QPushButton("Save Workflow", self)
        self.addItemButton = QPushButton("Add Item", self)
        self.removeItemButton = QPushButton("Remove Item", self)
        self.listView = QWidget(self)
        self.buttonView = QWidget(self)
        self.mainView = QWidget(self)

        self.apiInputDialog = AddAPIWindow(self)

        self.initUI()

    def initUI(self):
        self.setWindowTitle("My Application")
        self.setGeometry(100, 100, 1000, 800)

        self.setStyleSheet("""
/* QWidget form container */
QWidget {
    background-color: #f9f9f9;
    font-family: "Segoe UI", sans-serif;
    font-size: 14px;
}

/* QLabel */
QLabel {
    color: #333;
    margin-bottom: 4px;
}

/* QLineEdit, QTextEdit */
QLineEdit, QTextEdit {
    border: 1px solid #ccc;
    border-radius: 6px;
    padding: 8px 10px;
    background-color: #fff;
    color: #000;
}

QLineEdit:focus, QTextEdit:focus {
    border: 1px solid #0078d7;
    outline: none;
}

/* QPushButton */
QPushButton {
    background-color: #0078d7;
    color: white;
    padding: 8px 16px;
    border: none;
    border-radius: 6px;
}

QPushButton:hover {
    background-color: #005fa3;
}

QPushButton:pressed {
    background-color: #004d85;
}

QPushButton:disabled {
    background-color: #cccccc;
    color: #666666;
}

/* QComboBox */
QComboBox {
    padding: 6px 10px;
    border: 1px solid #ccc;
    border-radius: 6px;
    background-color: #fff;
}

/* QCheckBox */
QCheckBox {
    padding: 4px;
    spacing: 6px;
    color: #333;
}
""")

        # Create the main layout
        self.mainView.setGeometry(0, 0, 1000, 600)
        hbox = QHBoxLayout()
        hbox.addWidget(self.listView, 7)
        hbox.addWidget(self.buttonView, 3)
        self.mainView.setLayout(hbox)

        # Set up the API list view
        self.listView.setLayout(QVBoxLayout())
        self.listView.layout().setAlignment(Qt.AlignTop)

        # Set up the button view
        self.buttonView.setLayout(QVBoxLayout())

        functionButtonsView = QWidget()
        functionButtonsView.setLayout(QVBoxLayout())
        functionButtonsView.layout().setAlignment(Qt.AlignTop)
        functionButtonsView.layout().addWidget(self.addItemButton)
        self.removeItemButton.setDisabled(True)
        functionButtonsView.layout().addWidget(self.removeItemButton)

        self.buttonView.layout().addWidget(functionButtonsView, 8)
        self.buttonView.layout().addWidget(self.saveWorkflowButton, 2)

        # Set up the button press actions
        self.addItemButton.clicked.connect(self.addItem)
        self.addItemButton.setGeometry(50, 50, 100, 30)
        self.removeItemButton.clicked.connect(lambda: self.removeItem(self.CurrentItemName))



    def addItem(self):
        self.apiInputDialog.setWindowModality(Qt.ApplicationModal)
        self.apiInputDialog.show()
        class FocusLineEdit(QLineEdit):
            def focusInEvent(inner_self, event):
                print(inner_self.objectName())
                self.CurrentItemName = inner_self.objectName()
                self.removeItemButton.setEnabled(True)
                super().focusInEvent(event)

        item = FocusLineEdit(self)
        item.setObjectName(f"item_{self.Counter}")
        item.setPlaceholderText(f"Enter API endpoint")
        item.setGeometry(50, 100, 200, 30)
        item.setAlignment(Qt.AlignLeft)
        item.show()
        self.ItemList.append(item)
        self.listView.layout().addWidget(item)
        print("Item added:", self.ItemList)
        self.Counter += 1

    def removeItem(self, objectName):
        if objectName == "":
            print("No item selected to remove.")
            return
        for item in self.ItemList:
            if item.objectName() == objectName:
                self.ItemList.remove(item)
                self.listView.layout().removeWidget(item)
                item.deleteLater()
                print("Item removed:", objectName)
                self.Counter -= 1
                self.CurrentItemName = ""
                self.removeItemButton.setDisabled(True)
                break

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()