# -*- coding: utf-8 -*-
#@author: comet

import tkinter as tk
from tkinter import filedialog

class backupdiff(object):
    def __init__(self, pf1, pf2):
        pass

    def gleich(self):
        pass

    def nuralt(self):
        pass

    def nurneu(self):
        pass

def bu_check():
    pfadneu = filedialog.askdirectory()
    pfadalt = filedialog.askdirectory()
    bdiff = backupdiff(pfad1, pfad2)
    lgleich = bdiff.gleich() #Dateien in beiden Pfaden vorhanden
    lnuralt = bdiff.nuralt() #Dateien nur im Altverzeichnis
    lnurneu = bdiff.nurneu() #Dateien nur im Neuverzeichnis

if __name__== "__main__":
    version = '1.00'
    root = tk.Tk()
    menubar = tk.Menu(root)
    filemenu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Datei', underline=0, menu = filemenu)
    filemenu.add_command(label='Vergleichen', underline=0,
                         command='', accelerator='')
    filemenu.add_command(label='Beenden', underline=0,
                         command=root.destroy, accelerator='Alt+F4')
    root.config(menu = menubar)
    root.mainloop()
