import ttkbootstrap as ttk
from pages.mainpage import MainPage

page_data = [MainPage]

class App(ttk.Window):
    def __init__(self):
        super().__init__(themename = "journal")
        self.title("Ttk Bootstrap Example")

        self.geometry("600x300")
        self.minsize(600, 300)

        self.place_window_center()

        MainPage(self)

        self.mainloop()

if __name__ == "__main__":
    App()
