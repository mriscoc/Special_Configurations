#!/usr/bin/env python3
# ------------------------------------------------------------------------------
# Configurations generator script for the Professional Firmware
# Author: Miguel A. Risco Castillo
# URL: https://github.com/mriscoc/Special_Configurations
# version: 4.2
# date: 2023/05/23
# ------------------------------------------------------------------------------

from ast import Global
import os
import tkinter as tk
from tkinter import END,font,messagebox,ttk
import CreateConfigs

ConfigList = []

def fill_conf(obj):
  global ConfigList
  ConfigList.clear()
  ConfigList.append(obj.printer.get())
  ConfigList.append(obj.board.get())
  ConfigList.append(obj.leveling.get())
  if obj.ubl.get(): ConfigList.append("UBL")
  if not obj.display.get() == "DWIN": ConfigList.append(obj.display.get())
  if not obj.thermistor.get() == "T1": ConfigList.append(obj.thermistor.get())
  for checkbox in obj.featurelist:
    if checkbox.instate(['selected']): ConfigList.append(checkbox.cget("text"))

def set_conf():
    fill_conf(root)
    root.update_conf()
##    root.copy_clpbrd()

def generate_conf():
    global ConfigList
    fill_conf(root)
    root.update_conf()
    error = CreateConfigs.Generate(root.ConfigName.get(),ConfigList)
    if error:
        root.open_log()
    else:
        messagebox.showinfo(message="Configuration files generated", title="Professional Firmware")

def copy_clpbrd() :
    root.clipboard_clear()
    root.clipboard_append(root.Edit_GenFunc.get(1.0, END))
    messagebox.showinfo(message="Configuration generator was copied", title="Clipboard")

def auto_name():
    fill_conf(root)
    Name = '-'.join(ConfigList)
    #filter S1 printer name
    Name = Name.replace("-301F","-F").replace("F1-BLT","F1").replace("F4-BLT","F4")
    #filter UBL
    if "F1-UBL" not in Name and "F4-UBL" not in Name:
      Name = Name.replace("-UBL","UBL")
    #rename LinaAdv
    #Name = Name.replace("LinAdv","LA")
    root.ConfigName.delete(-1,END)
    root.ConfigName.insert(-1,Name)
    root.update_conf()

class Main(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=800, height=400)
        self.resizable(False, False)
        self.title("Professional Firmware Configurator")

        # configure style
        self.style = ttk.Style(self)
        self.style.configure('TLabel', font=('Helvetica', 9, 'bold'))

        self.topframe = ttk.Frame(self)
        self.topframe.grid(row=0,column=0, padx=10, pady=5, sticky="nw")
        self.leftframe = ttk.Frame(self)
        self.leftframe.grid(row=1,column=0, padx=10, pady=(5,0), sticky="nw")
        self.bottomframe = ttk.Frame(self, border=10)
        self.bottomframe.grid(row=2,column=0, columnspan=2, pady=0)

        # top frame--------------------------------------------------------------------------

        self.l1 = ttk.Label(self.topframe, text="Configuration Name:")
        self.l1.grid(row=0, column=0)

        self.ConfigName = ttk.Entry(self.topframe, width=60)
        self.ConfigName.insert(-1, "MyConfiguration")
        self.ConfigName.grid(row=0, column=1, padx=5)

        self.boton1 = ttk.Button(self.topframe, text="Auto", command=auto_name)
        self.boton1.grid(row=0, column=2)

        # left frame-------------------------------------------------------------------------

        self.l2 = ttk.Label(self.leftframe, text="Printer:", width=16)
        self.l2.grid(row=1, column=0, sticky="w")

        # Create the printerlist ------------------------------------------------------------
        self.printer = tk.StringVar(self,'Ender3V2')
        self.printerlist = []
        for file in os.listdir("_printers"):
            if file.endswith(".json") and not file.endswith("Common.json"):
                self.value = file.replace(".json", "")
                self.printerlist.append(ttk.Radiobutton(self.leftframe, text=self.value, variable=self.printer, value=self.value))

        # Add the radiobuttons to the window
        self.nrow = 2
        for self.radiobutton in self.printerlist:
            self.radiobutton.grid(row=self.nrow, column=0, sticky="w")
            self.nrow += 1

        #===================================================================================#

        self.l3 = ttk.Label(self.leftframe, text="Board:", width=15)
        self.l3.grid(row=1, column=1, sticky="w")

        # Create the boardlist
        self.board = tk.StringVar(self,'422')
        self.boardlist = []
        for file in os.listdir("_boards"):
            if file.endswith(".json"):
                self.value = file.replace(".json", "")
                self.boardlist.append(ttk.Radiobutton(self.leftframe, text=self.value, variable=self.board, value=self.value))

        # Add the radiobuttons to the window
        self.nrow = 2
        for self.radiobutton in self.boardlist:
            self.radiobutton.grid(row=self.nrow, column=1, sticky="w")
            self.nrow += 1

        #===================================================================================#

        self.l4 = ttk.Label(self.leftframe, text="Leveling:", width=14)
        self.l4.grid(row=1, column=2, sticky="w")

        # Create levelinglist
        self.leveling = tk.StringVar(self,'BLT')
        self.levelinglist = []
        for file in os.listdir("_leveling"):
            if file.endswith(".json") and not file.endswith("UBL.json"):
                self.value = file.replace(".json", "")
                self.levelinglist.append(ttk.Radiobutton(self.leftframe, text=self.value, variable=self.leveling, value=self.value, command=self.set_ubl))

        # Add the radiobuttons to the window
        self.nrow = 2
        for self.radiobutton in self.levelinglist:
            self.radiobutton.grid(row=self.nrow, column=2, sticky="w")
            self.nrow += 1

        # Add UBL checkbox
        self.ubl = tk.BooleanVar(self,True)
        self.ublchkb = ttk.Checkbutton(self.leftframe, text="UBL", variable=self.ubl)
        self.ublchkb.grid(row=self.nrow, column=2, sticky="w")

        #===================================================================================#

        self.l5 = ttk.Label(self.leftframe, text="Display:", width=12)
        self.l5.grid(row=1, column=3, sticky="w")

        # Create the displaylist
        self.display = tk.StringVar(self,'DWIN')
        self.displaylist = []
        for file in os.listdir("_displays"):
            if file.endswith(".json"):
                self.value = file.replace(".json", "")
                self.displaylist.append(ttk.Radiobutton(self.leftframe, text=self.value, variable=self.display, value=self.value))

        # Add the radiobuttons to the window
        self.nrow = 2
        for self.radiobutton in self.displaylist:
            self.radiobutton.grid(row=self.nrow, column=3, sticky="w")
            self.nrow += 1

        #===================================================================================#

        self.l6 = ttk.Label(self.leftframe, text="Thermistor:", width=12)
        self.l6.grid(row=1, column=4, sticky="w")

        # Create thermistorlist
        self.thermistor = tk.StringVar(self,'T1')
        self.thermistorlist = []
        for file in os.listdir("_thermistor"):
            if file.endswith(".json"):
                self.value = file.replace(".json", "")
                self.thermistorlist.append(ttk.Radiobutton(self.leftframe, text=self.value, variable=self.thermistor, value=self.value))

        # Add the radiobuttons to the window
        self.nrow = 2
        for self.radiobutton in self.thermistorlist:
            self.radiobutton.grid(row=self.nrow, column=4, sticky="w")
            self.nrow += 1

        #===================================================================================#

        self.l7 = ttk.Label(self.leftframe, text="Features:", width=12)
        self.l7.grid(row=1, column=5, sticky="w")

        # Create the featurelist
        self.featurelist = []
        for file in os.listdir("_features"):
            if file.endswith(".json"):
                self.featurelist.append(ttk.Checkbutton(self.leftframe, text=file.replace(".json", "")))

        # Add the checkboxes to the window
        self.nrow = 2
        for self.checkbox in self.featurelist:
            self.checkbox.grid(row=self.nrow, column=5, sticky="w")
            self.nrow += 1
            self.checkbox.state(['!alternate'])

        # bottom frame-------------------------------------------------------------------------

        self.img_boton = tk.PhotoImage(file="images/cog.png")
        self.boton2 = ttk.Button(self.bottomframe, text="Set config", image=self.img_boton, compound=tk.LEFT, command=set_conf)
        self.boton2.grid(row = 0, column=0, pady=(0,10))

        self.boton3 = ttk.Button(self.bottomframe, text="Generate", image=self.img_boton, compound=tk.LEFT, command=generate_conf)
        self.boton3.grid(row = 0, column=1, pady=(0,10))

        self.boton4 = ttk.Button(self.bottomframe, text="Copy to Clipboard", image=self.img_boton, compound=tk.LEFT, command=copy_clpbrd)
        self.boton4.grid(row = 0, column=2, pady=(0,10))

        self.Edit_GenFunc = tk.Text(self.bottomframe, width=73, height=2, relief='flat', bg="black", fg="yellow")
        fill_conf(self)
        self.update_conf()
        self.Edit_GenFunc.grid(row=1, column=0, columnspan=3, sticky="w")

        # ------------------------------------------------------------------------------------

    def update_conf(self):
        Name = self.ConfigName.get()
        self.Edit_GenFunc.delete(1.0, END)
        self.Edit_GenFunc.insert(END,f"CreateConfigs.Generate('{Name}',[")
        self.Edit_GenFunc.insert(END,','.join(f"'{item}'" for item in ConfigList))
        self.Edit_GenFunc.insert(END,"])")
    
    def set_ubl(self):
        if self.leveling.get()=="MM":
          self.ubl.set(0)
          self.ublchkb.configure(state='disabled')
        else:
          self.ublchkb.configure(state='enabled')

    def open_log(self):
      try:
        f = open(root.ConfigName.get()+"/log.txt","r")
        loglines = f.read()
        d = log_window(self)
        d.LogText.delete(1.0, END)
        d.LogText.insert(END, loglines)
        f.close()
      except Exception as e:
        messagebox.showinfo(message=str(e), title="Error")

class log_window(tk.Toplevel):
  def __init__(self, parent):
    super().__init__(parent)
    self.geometry("500x200")
    self.resizable(False, False)
    self.title("Error Log")
    self.LogText = tk.Text(self, height=10, relief='flat')
    self.LogText.pack()
    ttk.Button(self, text="OK", command=self.destroy).pack(expand=True)
    self.grab_set()


root = Main()
root.mainloop()
