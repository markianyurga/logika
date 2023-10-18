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
col2.addWidget(lb_note)
col2.addWidget(lst_note)
col2.addWidget(btn_note_cerelt)
col2.addWidget(btn_note_delete)
col2.addWidget(btn_note_sawe)
col2.addWidget(lb_tag)
col2.addWidget(lst_tag)
col2.addWidget(fild_tag)
col2.addWidget(btn_tag_add)
col2.addWidget(btn_tag_unpin)
col2.addWidget(btn_tag_search)

fild_tag.setPlaceholderText('відіть тег')

def add_teg():
    key = lst_note.currentItem().text()
    tag = fild_tag.text()
    
    lst_tag.addItem(tag)
    
 #  saveToFile()

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

def show_notes():
    key = lst_note.currentItem().text()
    print(notes[key]['текст'])

    fild_txt.setText(notes[key]['текст'])

with open('notes.json', 'r', encoding='utf8') as file:
    notes = json.load(file)

lst_note.addItems(notes)
lst_note.itemClicked.connect(show_notes)


windof.setLayout(loyout_notes)
windof.show()
app.exec_()