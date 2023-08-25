''' Вікно для картки питання '''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel, QSpinBox)
app = QApplication([])


btn_ok = QPushButton('відловісти')
btn_sleep = QPushButton('відпочити')
btn_menu = QPushButton('мнню')

lb_question = QLabel('')

box_minutes = QSpinBox()
box_minutes.setValue(5)

RadioGroupBox = QGroupBox('Варіанти відповідей')

RadioGroup = QButtonGroup()

r_bt1 = QRadioButton('')
r_bt2 = QRadioButton('')
r_bt3 = QRadioButton('')
r_bt4 = QRadioButton('')

RadioGroup.addButton(r_bt1)
RadioGroup.addButton(r_bt2)
RadioGroup.addButton(r_bt3)
RadioGroup.addButton(r_bt4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()

layout_ans2.addWidget(r_bt1)
layout_ans2.addWidget(r_bt2)

layout_ans3.addWidget(r_bt3)
layout_ans3.addWidget(r_bt4)

layout_ans1.addLayout(r_bt2)
layout_ans1.addLayout(r_bt3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox()
lb_result = QLabel('')
lb_correct = QLabel('')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_correct, alignment=Qt.AlignHCenter, stretch=2)

AnsGroupBox.setLayout(layout_res)

AnsGroupBox.hide()

layout_card = QVBoxLayout()
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line4 = QHBoxLayout()

layout_line1.addWidget(btn_menu)
layout_line1.addWidget(1)
layout_line1.addWidget(btn_sleep)
layout_line1.addWidget(box_minutes)

#layout_line1.addWidget(QLabel('хвилини'))

#layout_line2.addWiget(lb_question, alignment=(Qt.AlignHC))


# віджети, які треба буде розмістити:
# кнопка повернення в основне вікно 
# кнопка прибирає вікно і повертає його після закінчення таймера
# введення кількості хвилин
# кнопка відповіді "Ок" / "Наступний"
# текст питання

# Опиши групу перемикачів

# Опиши панень з результатами

# Розмісти весь вміст в лейаути. Найбільшим лейаутом буде layout_card

# Результат роботи цього модуля: віджети поміщені всередину layout_card, який можна призначити вікну.
def show_result():
    ''' показати панель відповідей '''
    pass

def show_question():
    ''' показати панель запитань '''
    pass