from PyQt6.QtWidgets import *
import hashlib
import os
import sys


def give_md5(path):
    filepath = os.open(path, os.O_RDONLY)
    md5 = hashlib.md5()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            md5.update(byte_block)
        print(md5.hexdigest())


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Obtain MD5")
        self.setGeometry(800, 100, 800, 100)
        textfield, search = QInputDialog().getText(self, "Get MD5", 'Paste a path to a file here.')

        if search and textfield:
            try:
                give_md5(textfield)
                sys.exit(1)
            except FileNotFoundError:
                print("please paste a valid file path.")
                sys.exit(404)
        else:
            sys.exit(2)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
