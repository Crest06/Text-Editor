import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file(root, text_edit):
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt")])
    if not filepath:
        return

    text_edit.delete(1.0, tk.END)
    with open(filepath, "r") as f:
        content = f.read()
        text_edit.insert(tk.END, content)
        root.title(f"Open File: {filepath}")

def save_file(root, text_edit):
    filepath = asksaveasfilename(filetypes=[("Text Files", "*.txt")])
    if not filepath:
        return

    with open(filepath, "w") as w:
        content = text_edit.get(1.0, tk.END)
        w.write(content)
        root.title(f"Save File: {filepath}")

def app():
    root = tk.Tk()
    root.title("Text Editor")

    root.rowconfigure(0, minsize=400)
    root.columnconfigure(0, minsize=500)

    text_edit = tk.Text(root, bg="white", font="Helvetica")
    text_edit.grid(row=0, column=1)

    frame = tk.Frame(root, relief=tk.RAISED, bd=2)
    save_button = tk.Button(frame, text="Save", padx=5, pady=5, command=lambda: save_file(root, text_edit))
    open_button = tk.Button(frame, text="Open", padx=5, pady=5, command=lambda: open_file(root, text_edit))
    save_button.grid(row=0, column=0)
    open_button.grid(row=0, column=1)
    frame.grid(row=0, column=0, sticky="ns")

    root.bind("<Control-s>", lambda x: save_file(root, text_edit))
    root.bind("<Control-o>", lambda x: open_file(root, text_edit))
    root.mainloop()

app()
