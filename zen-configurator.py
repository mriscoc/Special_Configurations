import os
import tkinter as tk
import CreateConfigs
from tkinter import ttk

# Create the window
window = tk.Tk()
window.title("~MriscoC Configurator UI by zenforic~")
window.geometry("500x500")
checked = []

# Create the checkboxes
checkboxes = []
working_path = os.path.realpath(__file__).replace(os.path.basename(__file__), "")
os.chdir(working_path)
for file in os.listdir(working_path):
    if file.endswith(".json"):
        checkboxes.append(ttk.Checkbutton(window, text=file.replace(".json", "")))

# Add the checkboxes to the window
for checkbox in checkboxes:
    checkbox.pack()
    checkbox.state(['!alternate'])

# Create the button
button = ttk.Button(window, text="Create Configs", command=lambda: CreateConfigs.Generate("Custom-zenUI", [check.cget("text") for check in checkboxes if check.instate(['selected'])]))
button.pack()


# Run the window
window.mainloop()