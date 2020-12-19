from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QPushButton
import sys
from pptx import Presentation
from PyQt5 import uic


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
        #uic.loadUi('Greeting window.ui', self)
        self.initUI()

    def initUI(self):
        print(1)
        self.setGeometry(300, 300, 900, 900)
        self.setWindowTitle('---')
        self.pushButton = QPushButton('Привет', self)
        self.pushButton.move(50, 50)
        self.pushButton.clicked.connect(self.create_presentation)
        self.pushButton.show()

    def create_presentation(self):
        print('180')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Greeting_window()
    ex.show()
    sys.exit(app.exec())
