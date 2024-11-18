import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
import tkinter as tk

class NewWindowApp(App):
    def on_start(self):

        root = tk.Tk()
        root.withdraw()  # Hide the root window
        screen_width = root.winfo_screenwidth() 
        screen_height = root.winfo_screenheight() -1

        # Define the desired window size
        Window.size = (screen_width, screen_height)
        Window.left = 0
        Window.top = 28
        Window.borderless = False

    def build(self):
        return

if __name__ == '__main__':
    NewWindowApp().run()