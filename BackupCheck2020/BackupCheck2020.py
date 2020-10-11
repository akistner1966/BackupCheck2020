# -*- coding: utf-8 -*-
#@author: comet

import tkinter as tk
from tkinter import filedialog
from tkinter import font as tkfont
import pickle as pkl
import os
import time
import datetime as dtme
import locale as lcl

class res_ausgabe(object):
    def __init__(self, parent, nuralt, gleich, nurneu, pfneu, pfalt):
        headlne = 'Backup-Vergleich - Stand: '
        headlne += dtme.datetime.now().strftime('%d.%m.%Y  %H:%M:%S')
        self.nuralt = nuralt
        self.gleich = gleich
        self.nurneu = nurneu
        self.pfneu = pfneu
        self.pfalt = pfalt
        self.bfnt = tkfont.Font(family='Helvetica', weight=tkfont.BOLD)
        self.nfnt = tkfont.Font(family='Helvetica')
        self.top = tk.Toplevel(parent)
        tk.Label(self.top, text=headlne).pack()
        self.bfnt = tkfont.Font(family='Helvetica', weight=tkfont.BOLD)
        self.nfnt = tkfont.Font(family='Helvetica')
        self.frameTop = tk.Frame(self.top) #Rahmen für Kopfzeile
        self.frameTop.pack(side=tk.TOP, fill=tk.BOTH)
        self.frameMid = tk.Frame(self.top) #Rahmen für Buttons
        self.frameMid.pack(side=tk.TOP, fill=tk.BOTH)
        self.frameDwn = tk.Frame(self.top) #Rahmen für Buttons
        self.frameDwn.pack(side=tk.TOP, fill=tk.BOTH)
        self.txthdln = tk.Text(self.frameTop, height=3, width=200)
        self.txthdln.pack(side=tk.LEFT, fill=tk.Y)
        self.vbar = tk.Scrollbar(self.frameMid)
        self.vbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.txtfeld = tk.Text(self.frameMid, height=40, width=200)
        self.txtfeld.pack(side=tk.LEFT, fill=tk.Y)
        self.vbar.config(command=self.txtfeld.yview)
        self.txtfeld.config(yscrollcommand=self.vbar.set)
        self.btnOK = tk.Button(self.frameDwn, text='OK', command=self._ok,
                               underline = 0)
        self.btnOK.pack(side=tk.LEFT, padx=5, pady=5)
        self.btnAlt = tk.Button(self.frameDwn, text='Nur alte Dateien',
                                   command=self._nuralt)
        self.btnAlt.pack(side=tk.LEFT, padx=5, pady=5)
        txtstr = 'Dateien, die in beiden Versionen vorkommen'
        self.btnGleich = tk.Button(self.frameDwn, text = txtstr,
                                   command=self._gleich)
        self.btnGleich.pack(side=tk.LEFT, padx=5, pady=5)
        self.btnNeu = tk.Button(self.frameDwn, text='Nur neue Dateien',
                                   command=self._nurneu)
        self.btnNeu.pack(side=tk.LEFT, padx=5, pady=5)
        self._gleich()
        self._btnconfig()

    def _ok(self):
        self.top.destroy()

    def _nuralt(self):
        self.txtfeld.delete("1.0","end")
        self._hdln('Nur alte Dateien', len(self.nuralt))
        for ele in self.nuralt:
            self.txtfeld.insert(tk.END, ele + '\n')
        self._btnconfig()

    def _gleich(self):
        self.txtfeld.delete("1.0","end")
        self._hdln('Dateien, die in beiden Versionen vorkommen',
                   len(self.gleich))
        for ele in self.gleich:
            self.txtfeld.tag_configure('black', foreground='#000000')
            self.txtfeld.tag_configure('red', foreground='#aa0000')
            self.txtfeld.tag_configure('green', foreground='#00aa00')
            pfgesneu = self.pfneu + '/' + ele
            pfgesalt = self.pfalt + '/' + ele
            ftneu = os.path.getmtime(pfgesneu)
            dgneu = os.path.getsize(pfgesneu)
            ftalt = os.path.getmtime(pfgesalt)
            dgalt = os.path.getsize(pfgesalt)
            self.txtfeld.insert(tk.END, ele, 'black')
            if ftneu == ftalt:
                self.txtfeld.insert(tk.END, ' (Datum identisch/',
                                    'green')
            else:
                self.txtfeld.insert(tk.END, ' (Datum nicht identisch/',
                                    'red')
            if dgneu == dgalt:
                self.txtfeld.insert(tk.END, ' Größe identisch)',
                                    'green')
            else:
                self.txtfeld.insert(tk.END, ' Größe nicht identisch)',
                                    'red')
            self.txtfeld.insert(tk.END, '\n', 'black')
        self._btnconfig()

    def _nurneu(self):
        self.txtfeld.delete("1.0","end")
        self._hdln('Nur neue Dateien', len(self.nurneu))
        for ele in self.nurneu:
            self.txtfeld.insert(tk.END, ele + '\n')
        self._btnconfig()

    def _hdln(self, txtstr, anzahl):
        self.txthdln.delete("1.0","end")
        txtstr += '(' + lcl.format('%d', anzahl, 1) + ' Dateien)\n'
        self.txthdln.insert(tk.END, txtstr)
        txtstr = 'Neues, aktuelles Verzeichnis: ' + self.pfneu + '\n'
        self.txthdln.insert(tk.END, txtstr)
        txtstr = 'Altes Verzeichnis im Backup: ' + self.pfalt
        self.txthdln.insert(tk.END, txtstr)

    def _btnconfig(self):
        self.btnOK.config(font=self.nfnt)
        self.btnAlt.config(font=self.nfnt)
        self.btnGleich.config(font=self.nfnt)
        self.btnNeu.config(font=self.nfnt)

class backupdiff(object):
    def __init__(self, pfalt, pfneu):
        self.pfalt = pfalt
        self.pfneu = pfneu
        self.lstalt = []
        self.lstneu = []
        self.gleichlst = []
        self.nuraltlst = []
        self.nurneulst = []
        for rootpath, dirs, files in os.walk(self.pfalt):
            for datei in files:
                self.lstalt.append(datei)
        for rootpath, dirs, files in os.walk(self.pfneu):
            for datei in files:
                self.lstneu.append(datei)
        self.lstalt.sort()
        self.lstneu.sort()
        for ele in self.lstalt:
            try:
                ndx = self.lstneu.index(ele)
                self.gleichlst.append(ele)
            except:
                self.nuraltlst.append(ele)
        for ele in self.lstneu:
            try:
                ndx = self.lstalt.index(ele)
            except:
                self.nurneulst.append(ele)

    def gleich(self):
        return(self.gleichlst)

    def nuralt(self):
        return(self.nuraltlst)

    def nurneu(self):
        return(self.nurneulst)

def bu_check(event=None):
    ttlstr = 'Neues, aktuelles Verzeichnis'
    pfadneu = filedialog.askdirectory(title=ttlstr)
    ttlstr = 'Altes Verzeichnis im Backup'
    pfadalt = filedialog.askdirectory(title=ttlstr)
    if pfadneu != '' and pfadalt != '':
        bdiff = backupdiff(pfadalt, pfadneu)
        altlst = bdiff.nuralt()
        gleichlst = bdiff.gleich()
        nurneu = bdiff.nurneu()
        resausg = res_ausgabe(root, altlst, gleichlst, nurneu,
                              pfadneu, pfadalt)

def progbeenden(event=None):
    pkllst = [pfadalt, pfadneu]
    fobj = open(pkldn, 'wb')
    pkl.dump(pkllst, fobj)
    fobj.close()
    root.quit()

if __name__== "__main__":
    version = '1.05' #globale Versionskonstante des Programms
    lcl.setlocale(lcl.LC_NUMERIC, '')
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
                         command=bu_check, accelerator='')
    filemenu.add_command(label='Beenden', underline=0,
                         command=progbeenden, accelerator='Alt+F4')
    root.config(menu = menubar)
    root.mainloop()