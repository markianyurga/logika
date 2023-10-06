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

loyout_notes = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()

loyout_notes.addLayout(col1, stretch=2)
loyout_notes.addLayout(col2, stretch=1)
col1.addWidget(fild_txt)
col2.addWidget(lb_note )lst_note btn_note_cerelt btn_note_delete btn_note_sawe lb_tag fild_tag btn_tag_add btn_tag_unpin btn_tag_search)
col2.addWidget(lst_note) btn_note_cerelt btn_note_delete btn_note_sawe lb_tag fild_tag btn_tag_add btn_tag_unpin btn_tag_search)
col2.addWidget(btn_note_cerelt) btn_note_delete btn_note_sawe lb_tag fild_tag btn_tag_add btn_tag_unpin btn_tag_search)

def add_teg():
    key = lst_note.currentItem().text()
    tag = field_tag.text()
    
    lst_tag.addItem(tag)
    
    saveToFile()

def del_teg():
    pass

def search_teg():
    tag = fild_tag.text()
    
    if 'шукати за тегом' ==btn_tag_search.text():
        filtered_notes = {}
        
        for key in notes:
            if tag in notes[key]['теги']:
                filtered_notes[key] = notes[key]
                
                
        btn_tag_search.setText("скинути пошук")  
         
        lst_note.clear()
        lst_note.addItems(notes)
        lst_tag.clear()
        fild_txt.clear()
    
    
    
    elif 'скинути тег' == btn_tag_search.text():
        btn_tag_search.setText('шукати тег')

with open('note.json', 'r', encoding='utf8') as file:
    notes = json.load(file)

windof.setLayout(loyout_notes)
windof.show()
app.exec_()