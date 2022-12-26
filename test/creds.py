import tkinter as tk
from tkinter import filedialog
import json
import sys

# Create the main window
root = tk.Tk()
root.title("File Path Specifier")


# Create a button that opens a File Dialog when clicked
def browse_file():
  file_path = filedialog.askopenfilename()
  success = tk.Label(root, text=file_path)
  file_path = {"creds_path":file_path}
  with open("creds_path.json", "w") as f:
    json.dump(file_path,f)
  success.pack()
  exit = tk.Label(root, text="Automatical exit after 3s")
  exit.pack()
  root.after(3000, lambda:root.destroy())

button = tk.Button(root, text="Browse", command=browse_file)
button.pack()

# Run the main loop
root.mainloop()