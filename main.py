import tkinter as tk
import urllib.request
from tkinter import messagebox

class Browser:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Python Browser")

        self.address_bar = tk.Entry(self.root)
        self.address_bar.pack(fill=tk.X)

        self.web_view = tk.Text(self.root)
        self.web_view.pack(fill=tk.BOTH, expand=True)

        self.address_bar.bind("<Return>", self.load_page)

        self.root.mainloop()

    def load_page(self, event=None):
        url = self.address_bar.get()
        try:
            response = urllib.request.urlopen(url)
            html = response.read()
            self.web_view.delete("1.0", tk.END)
            self.web_view.insert(tk.END, html)
        except:
            messagebox.showerror("Error", "Unable to load page")

browser = Browser()
