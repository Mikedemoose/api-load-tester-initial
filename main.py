import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtCore import Qt
from components.addAPI import AddAPIWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ItemList = []
        self.APIList = []
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

        self.apiInputDialog.dataSubmitted.connect(self.handleApiData)

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
                           
/* QTextEdit */
QTextEdit {
    border: 1.5px solid #b0b0b0;
    border-radius: 8px;
    padding: 10px 12px;
    background-color: #fcfcfc;
    color: #222;
    font-family: "Consolas", "Segoe UI", monospace;
    font-size: 15px;
    min-height: 100px;
}

QTextEdit:focus {
    border: 1.5px solid #0078d7;
    background-color: #fff;
}

/* QComboBox */
QComboBox {
    padding: 8px 12px;
    border: 1.5px solid #b0b0b0;
    border-radius: 8px;
    background-color: #fcfcfc;
    color: #222;
    font-size: 14px;
}

QComboBox:focus {
    border: 1.5px solid #0078d7;
    background-color: #fff;
}

QComboBox QAbstractItemView {
    border: 1.5px solid #0078d7;
    selection-background-color: #e6f2fb;
    selection-color: #222;
    background: #fff;
    font-size: 14px;
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
        # After dialog closes, add a QLabel with the API name if available
        if self.APIList:
            api_name = self.APIList[-1].get('apiName', 'Unnamed API')
            label = QLabel(api_name, self)
            label.setObjectName(f"item_{self.Counter}")
            label.setMinimumHeight(40)
            label.setStyleSheet("font-size: 16px; padding: 8px;")
            self.ItemList.append(label)
            self.listView.layout().addWidget(label)
            print("Item added:", self.ItemList)
            label.show()
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

    def handleApiData(self, data):
        print("Received API data:", data)
        self.APIList.append(data)
        print("Current API List:", self.APIList)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()