from PyQt5 import Qt, QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QPushButton
import sys
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
        font.setFamily('comic sans ms')  # меняет тип шрифта
        font.setPointSize(28)
        self.pushButton.setFont(font)
        self.pushButton.setGeometry(190, 500, 720, 300)
        self.pushButton.setStyleSheet(('''QPushButton {            
                                    background: rgb(184,232,176);
                                    position: absolute;
                                    border-radius: 70px;
                                    padding: 10px;
                                    color: rgb(255, 255, 255);
                                }'''))
        self.pushButton.clicked.connect(self.create_presentation)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(185, 300, 800, 111))
        self.label.setText('Добро пожаловать!')
        font = QtGui.QFont()
        font.setPointSize(200)
        self.label.setFont(QtGui.QFont("comic sans ms", 40, QtGui.QFont.Bold))
        self.label.setStyleSheet("color: rgb(184,232,176);")
        self.label.adjustSize() #???

    def create_presentation(self):
        self.k = ChooseTemplate([Slide(111, title='Привет')])
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
        self.pushButton.setStyleSheet('''QPushButton {            
                                    background: rgb(184,232,176);
                                    border-style: outset;
                                    border-width: 2px;
                                    border-radius: 15px;
                                    border-color: rgb(49,106,60) ;
                                    padding: 4px;
                                    color: rgb(255, 255, 255);
                                }''')   # параметры кнопки
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.clicked.connect(self.create_presentation)
        self.pushButton.show()

        layout = Qt.QGridLayout(self)

        for i in range(self.number_of_slides):
            x = QtWidgets.QPushButton(self)
            x.setGeometry(10, 70*i, 160, 100)
            x.setStyleSheet('''QPushButton {
                                    background: rgb(95,193,215);
                                    border-style: outset;
                                    border-width: 2px;
                                    border-radius: 25px;
                                    border-color: white ;
                                    padding: 4px;
                                    color: rgb(255, 255, 255);
                                }''')
            font = QtGui.QFont()
            font.setPointSize(14)
            x.setFont(font)
            x.setMaximumSize(160, 100)
            x.setMinimumSize(160, 100)
            x.setText(self.slides[i].title)
            layout.addWidget(x, i, 0)

        x = QtWidgets.QPushButton(self)
        x.setGeometry(10, 70*self.number_of_slides, 160, 100)
        x.setStyleSheet('''QPushButton {
                                    background: rgb(95,193,215);
                                    border-style: outset;
                                    border-width: 2px;
                                    border-radius: 25px;
                                    border-color: white ;
                                    padding: 4px;
                                    color: rgb(255, 255, 255);
                                }''')
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
        mw.setStyleSheet('background: rgb(95,193,215);')
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

class ChooseTemplate(MainScreen):
    def __init__(self, slides):
        super().__init__(slides)
        self.tempinit()

    def tempinit(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(250, 50, 300, 70))
        self.label.setText('Выберите макет слайда')
        font = QtGui.QFont()
        font.setPointSize(60)
        self.label.setFont(QtGui.QFont("comic sans ms", 30, QtGui.QFont.Bold))
        self.label.setStyleSheet("color: rgb(184,232,176);")
        self.label.adjustSize()

        tmp1 = QPushButton("1 template", self)
        tmp1.setGeometry(300, 200, 200, 100)
        tmp2 = QPushButton("2 template", self)
        tmp2.setGeometry(750, 200, 200, 100)
        tmp3 = QPushButton("3 template", self)
        tmp3.setGeometry(300, 650, 200, 100)
        tmp4 = QPushButton("4 template", self)
        tmp4.setGeometry(750, 650, 200, 100)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = GreetingWindow()
    ex.show()
    sys.exit(app.exec())