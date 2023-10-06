from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QLabel, 
    QListWidget, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QInputDialog,
    QTableWidget,  QListWidgetItem, QFormLayout, 
    QGroupBox, QButtonGroup, QRadioButton, QSpinBox)

import json

app = QApplication([])
windof = QWidget()

lb_note = QLabel('список заміток')
lst_note = QListWidget()
btn_note_cerelt = QPushButton('створити замітку')
btn_note_delete = QPushButton('видилити замітку')
btn_note_sawe = QPushButton('зберехти замітку')

lb_tag = QLabel('список тегів')
lst_tag = QListWidget()
fild_tag = QLineEdit()
btn_tag_add = QPushButton('додади тег')
btn_tag_unpin = QPushButton('відкріпити тег')
btn_tag_search = QPushButton('шукати за тегом')

fild_txt = QTextEdit()


windof.show()
app.exec_()