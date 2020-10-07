# -*- coding: utf-8 -*-
#@author: comet

import tkinter as tk
from tkinter import filedialog
import pickle as pkl
import os

class backupdiff(object):
    def __init__(self, pfalt, pfneu):
        self.pfalt = pfalt
        self.pfneu = pfneu
        for rootpath, dirs, files in os.walk(self.pfalt):
            for datei in files:
                pathname = rootpath + '\\' + datei
                dgroesse = os.path.getsize(pathname)
                ddattime = os.path.getmtime(pathname)
        for rootpath, dirs, files in os.walk(self.pfneu):
            for datei in files:
                pathname = rootpath + '\\' + datei
                dgroesse = os.path.getsize(pathname)
                ddattime = os.path.getmtime(pathname)

    def gleich(self):
        pass

    def nuralt(self):
        pass

    def nurneu(self):
        pass

def bu_check(event=None):
    pfadneu = filedialog.askdirectory()
    pfadalt = filedialog.askdirectory()
    bdiff = backupdiff(pfadalt, pfadneu)
    lgleich = bdiff.gleich() #Dateien in beiden Pfaden vorhanden
    lnuralt = bdiff.nuralt() #Dateien nur im Altverzeichnis
    lnurneu = bdiff.nurneu() #Dateien nur im Neuverzeichnis

def progbeenden(event=None):
    pkllst = [pfadalt, pfadneu]
    fobj = open(pkldn, 'wb')
    pkl.dump(pkllst, fobj)
    fobj.close()
    root.quit()

if __name__== "__main__":
    version = '1.01' #globale Versionskonstante des Programms
    pfadalt = ''
    pfadneu = ''
    pkldn = 'BackupCheck2020_dump.pkl'
    if os.path.isfile(pkldn):
        fobj = open(pkldn, 'rb')
        try:
            lst = pkl.load(fobj)
            pfadalt = lst[0]
            pfadneu = lst[1]
        except:
            pass
        fobj.close()
    root = tk.Tk()
    menubar = tk.Menu(root)
    filemenu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Datei', underline=0, menu = filemenu)
    filemenu.add_command(label='Vergleichen', underline=0,
                         command='', accelerator='')
    filemenu.add_command(label='Beenden', underline=0,
                         command=progbeenden, accelerator='Alt+F4')
    root.config(menu = menubar)
    root.mainloop()
