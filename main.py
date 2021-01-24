from PyQt5 import Qt, QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QPushButton
import sys
from PyQt5.QtGui import QPainter, QColor, QIcon


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
        self.k = ChooseTemplate([])
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
                                    background: rgb(13,174,78);
                                    border-style: outset;
                                    border-width: px;
                                    border-radius: 15px;
                                    border-color: rgb(49,106,60);
                                    padding: 4px;
                                    color: rgb(255, 255, 255);
                                }''')   # параметры кнопки
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.clicked.connect(self.create_presentation)
        self.pushButton.show()

        layout = Qt.QGridLayout(self)

        self.list_of_buttons = []

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
            self.list_of_buttons.append(x)
            layout.addWidget(x, i, 0)

        self.create_new_slide = QtWidgets.QPushButton(self)
        self.create_new_slide.setGeometry(10, 70*self.number_of_slides, 160, 100)
        self.create_new_slide.setStyleSheet('''QPushButton {      
                                    background: rgb(95,193,215);
                                    border-style: outset;
                                    border-width: 2px;
                                    border-radius: 25px;
                                    padding: 4px;
                                    color: rgb(255, 255, 255);
                                }''')  #border-style: outset;border-width: 2px;border-radius: 25px;padding: 4px;(параметры для границы(обводки))

        font = QtGui.QFont()
        font.setPointSize(50)
        self.create_new_slide.setFont(font)
        self.create_new_slide.setMaximumSize(160, 100)
        self.create_new_slide.setMinimumSize(160, 100)
        self.create_new_slide.setText('+')
        layout.addWidget(self.create_new_slide, self.number_of_slides, 0)

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
        for i in self.list_of_buttons:
            i.clicked.connect(self.to_slide)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(250, 50, 300, 70))
        self.label.setText('Выберите макет слайда')
        font = QtGui.QFont()
        font.setPointSize(60)
        self.label.setFont(QtGui.QFont("comic sans ms", 30, QtGui.QFont.Bold))
        self.label.setStyleSheet("color: rgb(184,232,176);")
        self.label.adjustSize()

        tmp1 = QPushButton("", self)
        tmp1.setGeometry(225, 200, 400, 300)
        tmp1.setIcon(QIcon('1.jpg'))
        tmp1.setIconSize(QSize(400, 300))
        tmp1.clicked.connect(self.to_template1)

        tmp2 = QPushButton("", self)
        tmp2.setGeometry(675, 200, 400, 300)
        tmp2.setIcon(QIcon('слайд2.jpg'))
        tmp2.setIconSize(QSize(400, 300))
        tmp2.clicked.connect(self.to_template2)

        tmp3 = QPushButton("", self)
        tmp3.setGeometry(225, 550, 400, 300)
        tmp3.setIcon(QIcon('слайд3.jpg'))
        tmp3.setIconSize(QSize(400, 300))

        tmp4 = QPushButton("", self)
        tmp4.setGeometry(675, 550, 400, 300)
        tmp4.setIcon(QIcon('слайд4.jpg'))
        tmp4.setIconSize(QSize(400, 300))

    def to_template1(self):
        self.slides.append(Slide(1))
        self.a = Template1(self.slides, len(self.slides) - 1)
        self.a.show()
        self.hide()

    def to_template2(self):
        self.slides.append(Slide(2))
        self.a = Template2(self.slides, len(self.slides) - 1)
        self.a.show()
        self.hide()

    def to_slide(self):
        sender = self.sender()
        i = self.list_of_buttons.index(sender)
        slide = self.slides[i]
        print(i)
        print(slide.type)
        if slide.type == 1:
            self.a = Template1(self.slides, i)
        elif slide.type == 2:
            self.a = Template2(self.slides, i)
        self.a.show()
        self.hide()


class Template1(MainScreen):
    def __init__(self, slides, number_of_slide):
        super().__init__(slides)
        self.number_of_slide = number_of_slide
        self.tempinit(number_of_slide)
        for i in self.list_of_buttons:
            i.clicked.connect(self.to_slide)

    def tempinit(self, number_of_slide):
        self.print_title = QtWidgets.QPlainTextEdit(self.slides[number_of_slide].title, self)
        self.print_title.setGeometry(300, 150, 700,  250)

        self.print_text = QtWidgets.QPlainTextEdit(self.slides[number_of_slide].text, self)
        self.print_text.setGeometry(300, 450, 700, 200)

        self.create_new_slide.clicked.connect(self.new_slide)

    def paintEvent(self, event):
        self.border = QPainter()
        self.border.begin(self)
        self.draw(event, self.border)
        self.border.end()

    def draw(self, event, border):
        border.setBrush(QColor(184, 232, 176))
        border.setPen(QColor(184, 232, 176))
        border.drawRoundedRect(250, 100, 800, 700, 50, 50)

    def new_slide(self):
        self.slides[self.number_of_slide].set_title(self.print_title.toPlainText())
        self.slides[self.number_of_slide].set_text(self.print_text.toPlainText())
        self.a = ChooseTemplate(self.slides)
        self.a.show()
        self.hide()

    def to_slide(self):
        self.slides[self.number_of_slide].set_title(self.print_title.toPlainText())
        self.slides[self.number_of_slide].set_text(self.print_text.toPlainText())
        sender = self.sender()
        i = self.list_of_buttons.index(sender)
        slide = self.slides[i]
        print(i)
        print(slide.type)
        if slide.type == 1:
            self.a = Template1(self.slides, i)
        elif slide.type == 2:
            self.a = Template2(self.slides, i)
        self.a.show()
        self.hide()


class Template2(MainScreen):
    def __init__(self, slides, number_of_slide):
        super().__init__(slides)
        self.number_of_slide = number_of_slide
        self.tempinit(number_of_slide)
        for i in self.list_of_buttons:
            i.clicked.connect(self.to_slide)

    def tempinit(self, number_of_slide):
        self.print_title = QtWidgets.QPlainTextEdit(self.slides[number_of_slide].title, self)
        self.print_title.setGeometry(300, 150, 700,  150)

        self.print_text = QtWidgets.QPlainTextEdit(self.slides[number_of_slide].text, self)
        self.print_text.setGeometry(300, 350, 700, 400)

        self.create_new_slide.clicked.connect(self.new_slide)

    def paintEvent(self, event):
        self.border = QPainter()
        self.border.begin(self)
        self.draw(event, self.border)
        self.border.end()

    def draw(self, event, border):
        border.setBrush(QColor(184, 232, 176))
        border.setPen(QColor(184, 232, 176))
        border.drawRoundedRect(250, 100, 800, 700, 50, 50)

    def new_slide(self):
        self.slides[self.number_of_slide].set_title(self.print_title.toPlainText())
        self.slides[self.number_of_slide].set_text(self.print_text.toPlainText())
        self.a = ChooseTemplate(self.slides)
        self.a.show()
        self.hide()

    def to_slide(self):
        self.slides[self.number_of_slide].set_title(self.print_title.toPlainText())
        self.slides[self.number_of_slide].set_text(self.print_text.toPlainText())
        sender = self.sender()
        i = self.list_of_buttons.index(sender)
        slide = self.slides[i]
        print(i)
        print(slide.type)
        if slide.type == 1:
            self.a = Template1(self.slides, i)
        elif slide.type == 2:
            self.a = Template2(self.slides, i)
        self.a.show()
        self.hide()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = GreetingWindow()
    ex.show()
    sys.exit(app.exec())