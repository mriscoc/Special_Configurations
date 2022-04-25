import os
import shutil
import sys
import threading
import tkinter as tk
import CreateConfigs
from tkinter import ttk

class ConsoleText(tk.Text): # Class derived from https://stackoverflow.com/questions/3333334/stdout-to-tkinter-gui
    '''A Tkinter Text widget that provides a scrolling display of console
    stderr and stdout.'''

    class IORedirector(object):
        '''A general class for redirecting I/O to this Text widget.'''
        def __init__(self,text_area):
            self.text_area = text_area

    class StdoutRedirector(IORedirector):
        '''A class for redirecting stdout to this Text widget.'''
        def write(self,str):
            self.text_area.write(str,False)

    class StderrRedirector(IORedirector):
        '''A class for redirecting stderr to this Text widget.'''
        def write(self,str):
            self.text_area.write(str,True)

    def __init__(self, master=None, cnf={}, **kw):
        '''See the __init__ for Tkinter.Text for most of this stuff.'''

        tk.Text.__init__(self, master, cnf, **kw)

        self.started = False
        self.write_lock = threading.Lock()

        self.tag_configure('STDOUT',background='white',foreground='black')
        self.tag_configure('STDERR',background='white',foreground='red')

        self.config(state=tk.NORMAL)
        self.bind('<Key>',lambda e: 'break') #ignore all key presses

        self.config(state=tk.DISABLED)

    def start(self):

        if self.started:
            return

        self.started = True

        self.original_stdout = sys.stdout
        self.original_stderr = sys.stderr

        stdout_redirector = ConsoleText.StdoutRedirector(self)
        stderr_redirector = ConsoleText.StderrRedirector(self)

        sys.stdout = stdout_redirector
        sys.stderr = stderr_redirector

    def stop(self):

        if not self.started:
            return

        self.started = False

        sys.stdout = self.original_stdout
        sys.stderr = self.original_stderr

    def write(self,val,is_stderr=False):

        #Fun Fact:  The way Tkinter Text objects work is that if they're disabled,
        #you can't write into them AT ALL (via the GUI or programatically).  Since we want them
        #disabled for the user, we have to set them to NORMAL (a.k.a. ENABLED), write to them,
        #then set their state back to DISABLED.

        self.write_lock.acquire()
        self.config(state=tk.NORMAL)

        self.insert('end',val,'STDERR' if is_stderr else 'STDOUT')
        self.see('end')

        self.config(state=tk.DISABLED)
        self.write_lock.release()

# Create the window
window = tk.Tk()
window.title("~MriscoC Configurator UI by zenforic~")
window.geometry("700x700")
prev_stdout = sys.stdout
prev_stderr = sys.stderr

# Create the checkboxes
checkboxes = []
working_path = os.path.realpath(__file__).replace(os.path.basename(__file__), "")
os.chdir(working_path)
for file in os.listdir(working_path):
    if file.endswith(".json") and not file.endswith("Common.json"):
        checkboxes.append(ttk.Checkbutton(window, text=file.replace(".json", "")))

# Add the checkboxes to the window
for checkbox in checkboxes:
    checkbox.pack()
    checkbox.state(['!alternate'])

# Create the text widget
text = ConsoleText(window, height=10, width=85)
text.pack()
text.start()

# Create the buttons
button = ttk.Button(window, text="Create Configs", command=lambda: CreateConfigs.Generate("Custom-zenUI", [check.cget("text") for check in checkboxes if check.instate(['selected'])]))
button.pack()
buttonD = ttk.Button(window, text="Delete Configs", command=lambda: shutil.rmtree("Custom-zenUI"))
buttonD.pack()
buttonQ = ttk.Button(window, text="Quit", command=lambda: window.destroy())
buttonQ.pack()


# Run the window
window.mainloop()
sys.stdout = prev_stdout # when the window closes, text.stop() cannot be called because it is destroyed. This will restore stdout.
sys.stderr = prev_stderr
