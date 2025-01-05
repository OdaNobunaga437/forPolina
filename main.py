import sys
import sqlite3

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QCalendarWidget, QTimeEdit

con = sqlite3.connect('registration.db')
cur = con.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS registrations (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
date TEXT NOT NULL,
time TEXT NOT NULL
)
''')


class SimplePlanner(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('055.ui', self)
        self.setGeometry(300, 300, 700, 700)
        self.setWindowTitle('Минипланировщик')
        self.addEventBtn.clicked.connect(self.start)
        self.outputButton.clicked.connect(self.output)
        self.eventList.setSortingEnabled(True)

    def start(self):
        date = self.calendarWidget.selectedDate().toString("yyyy-MM-dd")
        time = self.timeEdit.time().toString()
        name = self.lineEdit.text()
        cur.execute('INSERT INTO registrations(name, date, time) VALUES (?, ?, ?)',
                    (name, date, time)).fetchall()
        con.commit()

    def output(self):
        date = self.calendarWidget.selectedDate().toString("yyyy-MM-dd")
        regs = cur.execute('SELECT * FROM registrations WHERE date = ?', (date,)).fetchall()
        self.eventList.clear()
        for reg in regs:
            self.eventList.addItem(f'{reg[2]} {reg[3]} - {reg[1]}')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SimplePlanner()
    ex.show()
    sys.exit(app.exec())
