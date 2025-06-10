import tkinter as tk
from GUI.App import FileSelectorApp

# GUI 실행
if __name__ == "__main__":
    root = tk.Tk()
    app = FileSelectorApp(root)
    root.mainloop()