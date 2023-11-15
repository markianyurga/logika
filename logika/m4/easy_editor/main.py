from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap 

from PIL import Image, ImageFilter

import os

app = QApplication([])
window = QWidget()
window.resize(700, 500)

btn_papka = QPushButton('папка')
btn_vlivo = QPushButton('вліво')
btn_vpravo = QPushButton('вправо')
btn_dzerkalo = QPushButton('дзеркало')
btn_rizkicnm = QPushButton('різкість')
btn_bw = QPushButton('чб')

lst_fils = QListWidget()
lb_pic = QLabel("картина")

leut = QHBoxLayout()
row = QHBoxLayout()

col1 = QVBoxLayout()
col2 = QVBoxLayout()

leut.addLayout(col1, 1)
leut.addLayout(col2, 4)

row.addWidget(btn_vlivo)
row.addWidget(btn_vpravo)
row.addWidget(btn_dzerkalo)
row.addWidget(btn_rizkicnm)
row.addWidget(btn_bw)

col1.addWidget(btn_papka)
col1.addWidget(lst_fils)

col2.addWidget(lb_pic)
col2.addLayout(row)
    
def showfaulneumlest():
    workdir = QFileDialog.getExistingDirectory()
    
btn_papka.clicked.connect(showfaulneumlest)

window.setLayout(leut)
window.show()
app.exec_()