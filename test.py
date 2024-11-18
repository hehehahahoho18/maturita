from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
def BreakTesterApp(App):
    def build(self):
        mainLayout = BoxLayout(orientation= 'vertical')
        return mainLayout
def MainApp():
    BreakTesterApp().run()
if __name__ == "__main__":
    popup = Popup(title='Test popup', content=Label(text='Hello world'),auto_dismiss=False)
    popup.bind(on_dissmiss=MainApp)
    popup.open()