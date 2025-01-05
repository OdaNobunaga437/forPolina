import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow


class AntiPlagiarism(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('05.ui', self)
        self.setGeometry(300, 300, 800, 700)
        self.setWindowTitle('Антиплагиат v0.0001')
        self.status_bar = self.statusBar()
        self.checkBtn.clicked.connect(self.start)

    def start(self):
        tex1 = set(self.text1.toPlainText().split('\n'))
        tex2 = set(self.text2.toPlainText().split('\n'))

        # intersection = len(tex1 & tex2)
        # union = len(tex1 | tex2)

        itog = float(f'{len(tex1 & tex2) / len(tex1 | tex2) * 100:0.2f}')
        porog = self.alert_value.value()

        if itog >= porog:
            self.status_bar.showMessage(f'Тексты похожи на {f"{itog:0.2f}"}%, плагиат')
        else:
            self.status_bar.showMessage(f'Тексты похожи на {f"{itog:0.2f}"}%, не плагиат')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AntiPlagiarism()
    ex.show()
    sys.exit(app.exec())
