import asyncio
import httpx
from PyQt5.QtWidgets import (QLineEdit, QPushButton, QMessageBox, QDialog, QWidget,
                             QFormLayout, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea)
from PyQt5.QtCore import Qt
from components.apiComponents.headerInput import HeaderInput
from components.headersList import HeaderList
from components.apiComponents.apiBar import ApiBar

class AddAPIWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.fullData = {}
        self.addButton = QPushButton("Add API", self)
        self.centralForm = QWidget(self)
        self.apiBar = ApiBar(self)
        self.headersListView = QWidget(self)
        self.scrollArea = QScrollArea(self)
        self.headersItems = HeaderList(self)
        self.payloadInput = QLineEdit(self)
        self.addHeadersButton = QPushButton("Add Header", self)
        self.initUi()

    def initUi(self):
        self.setWindowTitle("Add API")
        self.setGeometry(200, 200, 700, 500)

        self.initCentralForm()
        self.initAddButton()

    def initCentralForm(self):
        self.centralForm.setGeometry(50, 50, 600, 350)
        self.centralForm.setLayout(QFormLayout())
        self.centralForm.layout().addRow("API Name:", QLineEdit())
        self.centralForm.layout().addRow(self.apiBar)
        self.initHeadersListView()

    def initAddButton(self):
        self.addButton.setGeometry(150, 430, 100, 40)
        self.addButton.clicked.connect(self.addAPI)

    def addAPI(self):
        print("API added successfully!")
        print(self.apiBar.getData())
        print(self.headersItems.getHeadersList())
        self.fullData = {
            "apiName": self.centralForm.layout().itemAt(0).widget().text(),
            "apiMethod": self.apiBar.apiMethodText,
            "apiUrl": self.apiBar.apiUrlText,
            "headers": self.headersItems.getHeadersList()
        }
        print("Full Data:", self.fullData)
        # asyncio.run(callAPI(self.fullData))
        QMessageBox.information(self, "Info", "API added successfully!")
        self.close()

    def initHeadersListView(self):
        # overall headers list view
        self.headersListView.setGeometry(50, 400, 300, 100)
        self.headersListView.setLayout(QHBoxLayout())

        # button menu
        buttonMenu = QWidget()
        buttonMenu.setLayout(QVBoxLayout())
        buttonMenu.layout().setAlignment(Qt.AlignTop)
        buttonMenu.layout().addWidget(self.addHeadersButton)

        # headers list
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.headersItems)
        self.headersListView.layout().addWidget(self.scrollArea, 8)
        self.headersListView.layout().addWidget(buttonMenu, 2)
        self.centralForm.layout().addRow(QLabel("Headers:"))
        self.centralForm.layout().addRow(self.headersListView)

        def addHeader():
            self.headersItems.addHeaderInput()

        self.addHeadersButton.clicked.connect(addHeader)


async def callAPI(apiData):
    # This function would handle the API call using the data from the dialog
    print("Calling API with data:", apiData)
    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=apiData['apiMethod'],
            url=apiData['apiUrl'],
            headers=dict(apiData['headers']),
            # data=apiData.get('payload', None)
        )
        print("Response:", response.text)
        return response

    # Here you would implement the actual API call logic
    pass