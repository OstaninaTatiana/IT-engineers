from PyQt5 import QtWidgets
import sys
from pptx import Presentation
from PyQt5 import uic


class MyWidget(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Greeting window.ui', self)
        self.initUI()

    def initUI(self):
        self.pushButton.clicked.connect(self.create_presentation)

    def create_presentation(self):
        print('Hello')
        self.presentation = Presentation()
        title_slide_layout = self.presentation.slide_layouts[0]
        slide = self.presentation.slides.add_slide(title_slide_layout)
        title = slide.shapes.title
        subtitle = slide.placeholders[1]

        title.text = "Hello, World!"
        subtitle.text = "Презентация создана"
        self.presentation.save('Презентация1.pptx')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
