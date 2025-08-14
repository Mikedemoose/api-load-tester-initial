import asyncio
import httpx
from PyQt5.QtWidgets import (QLineEdit, QPushButton, QMessageBox, QDialog, QWidget,
                             QFormLayout, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea)
from PyQt5.QtCore import Qt, pyqtSignal
from components.apiComponents.headerInput import HeaderInput
from components.headersList import HeaderList
from components.apiComponents.apiBar import ApiBar
from components.payloadInput import PayloadInput

class AddAPIWindow(QDialog):
    dataSubmitted = pyqtSignal(dict)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.fullData = {}
        self.addButton = QPushButton("Add API", self)
        self.centralForm = QWidget(self)
        self.apiBar = ApiBar(self)
        self.headersListView = QWidget(self)
        self.scrollArea = QScrollArea(self)
        self.headersAndPayloadView = QWidget(self)
        self.headersItems = HeaderList(self)
        self.payloadInput = PayloadInput(self)
        self.addHeadersButton = QPushButton("Add Header", self)
        self.initUi()

    def initUi(self):
        self.setWindowTitle("Add API")
        self.setGeometry(100, 100, 1000, 800)  # Increased window size

        self.initCentralForm()
        self.initAddButton()

    def initCentralForm(self):
        self.centralForm.setGeometry(50, 50, 900, 600)  # Increased central form size
        self.centralForm.setLayout(QFormLayout())
        api_name_edit = QLineEdit()
        api_name_edit.setMinimumWidth(400)
        api_name_edit.setMinimumHeight(40)
        self.centralForm.layout().addRow("API Name:", api_name_edit)
        self.apiBar.setMinimumHeight(60)
        self.centralForm.layout().addRow(self.apiBar)
        self.initHeadersListView()

    def initAddButton(self):
        self.addButton.setGeometry(300, 700, 200, 60)  # Larger button
        self.addButton.setMinimumWidth(200)
        self.addButton.setMinimumHeight(60)
        self.addButton.clicked.connect(self.addAPI)

    def addAPI(self):
        print("API added successfully!")
        print(self.apiBar.getData())
        print(self.headersItems.getHeadersList())
        self.fullData = {
            "apiName": self.centralForm.layout().itemAt(1).widget().text(),
            "apiMethod": self.apiBar.apiMethodText,
            "apiUrl": self.apiBar.apiUrlText,
            "headers": self.headersItems.getHeadersList()
        }
        print("Full Data:", self.fullData)
        self.dataSubmitted.emit(self.fullData)
        # asyncio.run(callAPI(self.fullData))
        QMessageBox.information(self, "Info", "API added successfully!")
        self.close()

    def initHeadersListView(self):
        self.headersAndPayloadView.setGeometry(50, 200, 800, 400)  # Larger area
        self.headersAndPayloadView.setLayout(QVBoxLayout())
        self.headersAndPayloadView.layout().setAlignment(Qt.AlignTop)

        # overall headers list view
        self.headersListView.setGeometry(50, 400, 600, 200)  # Larger headers list view
        self.headersListView.setLayout(QHBoxLayout())

        # button menu
        buttonMenu = QWidget()
        buttonMenu.setLayout(QVBoxLayout())
        buttonMenu.layout().setAlignment(Qt.AlignTop)
        self.addHeadersButton.setMinimumWidth(150)
        self.addHeadersButton.setMinimumHeight(40)
        buttonMenu.layout().addWidget(self.addHeadersButton)

        # headers list
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setMinimumWidth(500)
        self.scrollArea.setMinimumHeight(200)
        self.headersItems.setMinimumWidth(500)
        self.headersItems.setMinimumHeight(200)
        self.scrollArea.setWidget(self.headersItems)

        self.headersAndPayloadView.layout().addWidget(self.scrollArea, 5)
        self.payloadInput.setMinimumHeight(200)
        self.payloadInput.setMinimumWidth(500)
        self.headersAndPayloadView.layout().addWidget(self.payloadInput, 5)

        self.headersListView.layout().addWidget(self.headersAndPayloadView, 8)
        self.headersListView.layout().addWidget(buttonMenu, 2)
        label = QLabel("Headers:")
        label.setMinimumHeight(30)
        label.setMinimumWidth(200)
        self.centralForm.layout().addRow(label)
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