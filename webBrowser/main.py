from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

class browserClass(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(browserClass, self).__init__(*args, **kwargs)

        self.window = QWidget()
        self.window.setWindowTitle("Souper")

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.urlBar = QLineEdit()
        self.urlBar.setFixedHeight(30)

        font = QFont()
        font.setPointSize(10)
        self.urlBar.setFont(font)

        #self.urlBar.setWordWrapMode(QTextOption.NoWrap)
        self.urlBar.setAlignment(Qt.AlignVCenter)
        self.urlBar.returnPressed.connect(lambda: self.navigate(self.urlBar.text()))

        self.goBtn = QPushButton("Go")
        self.goBtn.setMinimumHeight(30)

        self.backBtn = QPushButton("<")
        self.backBtn.setMinimumHeight(30)

        self.forwardBtn = QPushButton(">")
        self.forwardBtn.setMinimumHeight(30)

        self.horizontal.addWidget(self.urlBar)
        self.horizontal.addWidget(self.goBtn)
        self.horizontal.addWidget(self.backBtn)
        self.horizontal.addWidget(self.forwardBtn)

        self.browser = QWebEngineView()
        self.goBtn.clicked.connect(lambda: self.navigate(self.urlBar.text()))
        self.backBtn.clicked.connect(self.browser.back)
        self.forwardBtn.clicked.connect(self.browser.forward)
        
        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("https://google.com"))

        self.window.setLayout(self.layout)
        self.window.showMaximized()
    
    def navigate(self, url):
        url = url.strip()
        if " " in url:
            url = "www.google.com/search?q=" + "+".join(url.split())
            self.urlBar.setText(url)
        if not(url.startswith("https")):
            url = "http://" + url
            self.urlBar.setText(url)
        self.browser.setUrl(QUrl(url))

app = QApplication([])
window = browserClass()
app.exec_()