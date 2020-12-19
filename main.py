from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QPushButton
import sys
from pptx import Presentation
from PyQt5 import uic
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QMessageBox


class Greeting_window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Greeting_window.ui', self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Презентация')
        self.pushButton.clicked.connect(self.create_presentation)

    def create_presentation(self):
        self.k = Choose_template([])
        self.k.show()
        self.hide()

        #print('Hello')
        #self.presentation = Presentation()
        #title_slide_layout = self.presentation.slide_layouts[0]
        #slide = self.presentation.slides.add_slide(title_slide_layout)
        #title = slide.shapes.title
        #subtitle = slide.placeholders[1]

        #title.text = "Hello, World!"
        #subtitle.text = "Презентация создана"
        #self.presentation.save('Презентация1.pptx')


class Choose_template(QtWidgets.QMainWindow):
    def __init__(self, slides):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 30, 1100, 900)
        self.setWindowTitle('Презентация')

        self.pushButton = QPushButton('Готово', self)
        self.pushButton.setGeometry(20, 850, 90, 40)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.clicked.connect(self.create_presentation)
        self.pushButton.show()

    def create_presentation(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open a file', 'C://')
        QMessageBox.information(self, '..', file_name)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Greeting_window()
    ex.show()
    sys.exit(app.exec())
