from PyQt5 import Qt, QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QPushButton
import sys
from pptx import Presentation
from  PyQt5.QtGui import QPainter, QColor


class Slide():
    def __init__(self, type, title='', text='', picture=''):
        self.type = type
        self.text = text
        self.title = title
        self.picture = picture

    def set_text(self, text):
        self.text = text

    def set_title(self, text):
        self.title = text

    def set_picture(self, picture):
        self.picture = picture


class GreetingWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 30, 1100, 900)
        self.setWindowTitle('Презентация')

        self.pushButton = QPushButton(self)
        self.pushButton.setText('Создать презентацию')
        font = QtGui.QFont()
        font.setPointSize(28)
        self.pushButton.setFont(font)
        self.pushButton.setGeometry(190, 600, 720, 80)
        self.pushButton.clicked.connect(self.create_presentation)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(185, 300, 800, 111))
        self.label.setText('Добро пожаловать!')
        font = QtGui.QFont()
        font.setPointSize(60)
        self.label.setFont(font)

    def create_presentation(self):
        self.k = MainScreen([Slide(111, title='Привет')])
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


class MainScreen(QtWidgets.QMainWindow):
    def __init__(self, slides):
        super().__init__()
        self.slides = slides
        self.number_of_slides = len(self.slides)
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

        layout = Qt.QGridLayout(self)

        for i in range(self.number_of_slides):
            x = QtWidgets.QPushButton(self)
            x.setGeometry(10, 70*i, 160, 100)
            font = QtGui.QFont()
            font.setPointSize(14)
            x.setFont(font)
            x.setMaximumSize(160, 100)
            x.setMinimumSize(160, 100)
            x.setText(self.slides[i].title)
            layout.addWidget(x, i, 0)

        x = QtWidgets.QPushButton(self)
        x.setGeometry(10, 70*self.number_of_slides, 160, 100)
        font = QtGui.QFont()
        font.setPointSize(50)
        x.setFont(font)
        x.setMaximumSize(160, 100)
        x.setMinimumSize(160, 100)
        x.setText('+')
        layout.addWidget(x, self.number_of_slides, 0)

        w = Qt.QWidget(self)
        w.setLayout(layout)

        mw = Qt.QScrollArea(self)
        mw.setWidget(w)
        mw.resize(200, 830)
        mw.show()

    def paintEvent(self, event):
        self.qp = QPainter()
        self.qp.begin(self)
        self.draw(event, self.qp)
        self.qp.end()

    def draw(self, event, qp):
        qp.setPen(QColor(0, 0, 0))
        qp.drawRect(0, 0, 200, 900)

    def create_presentation(self):
        print(1)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = GreetingWindow()
    ex.show()
    sys.exit(app.exec())
