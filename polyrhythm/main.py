from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Polythythm")
        self.setFixedSize(400,400)

        button = QPushButton("click me")
        button.setCheckable(False)

app = QApplication([])
window = mainWindow()

window.show()

app.exec()
