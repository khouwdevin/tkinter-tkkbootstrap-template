import ttkbootstrap as ttk
from ttkbootstrap.constants import INFO, OUTLINE

class MainPage(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        label = ttk.Label(text ="Main Page", font = "TimesNewRoman 18 bold")
        label.pack(pady = 10)

        self.button = ttk.Button(text = "Download", bootstyle=(INFO, OUTLINE))
        self.button.pack(pady = 10)
