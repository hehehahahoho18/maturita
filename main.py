import kivy
from kivy.app import App
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
import subprocess
import sys
from kivy.clock import Clock
import json

class AnimatedToggleButton(ToggleButton):
    def on_state(self, widget, value):
        # Animate the button size when pressed or released
        if value == 'down':
            anim = Animation(size=(225, 45), duration=0.2)  # Scale up
        else:
            anim = Animation(size=(250, 50), duration=0.2)  # Scale down
        anim.start(self)

class SubmitButton(Button):
    pass

class CheckboxApp(App):
    
    def build(self):
        # Set window properties
        Window.size = (600, 400)
        self.layout = FloatLayout()

        # Set the background color to dark gray
        with self.layout.canvas.before:
            Color(0.1, 0.1, 0.1, 1)  # Darker gray color (RGBA)
            self.rect = Rectangle(size=self.layout.size, pos=self.layout.pos)

        # Update the rectangle size when the layout is resized
        self.layout.bind(size=self._update_rect, pos=self._update_rect)

        # Create toggle buttons to act as checkboxes
        self.toggle1 = AnimatedToggleButton(text='Drive 1', size_hint=(None, None), size=(250, 50), pos_hint={'center_x': 0.5, 'y': 0.75})
        self.toggle2 = AnimatedToggleButton(text='Drive 2', size_hint=(None, None), size=(250, 50), pos_hint={'center_x': 0.5, 'y': 0.55})
        self.toggle3 = AnimatedToggleButton(text='Drive 3', size_hint=(None, None), size=(250, 50), pos_hint={'center_x': 0.5, 'y': 0.35})

        # Add toggle buttons to the layout
        self.layout.add_widget(self.toggle1)
        self.layout.add_widget(self.toggle2)
        self.layout.add_widget(self.toggle3)

        # Create submit button
        self.submit_button = SubmitButton(text='Choose', size_hint=(None, None), size=(100, 50), pos_hint={'center_x': 0.5, 'y': 0.1})
        self.submit_button.bind(on_press=self.on_submit)
        self.layout.add_widget(self.submit_button)

        return self.layout

    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

    def on_submit(self, instance):
        selected_items = []
        if self.toggle1.state == 'down':
            selected_items.append('Drive 1')
        if self.toggle2.state == 'down':
            selected_items.append('Drive 2')
        if self.toggle3.state == 'down':
            selected_items.append('Drive 3')

#Check if the selected_items array is empty
        if not selected_items:
            popup = Popup(title='Selected_null',content=Label(text='No drives selected.'),
                size_hint=(None, None), size=(400, 200))
            popup.open()
        else:
#Sending selected_items into data.json

        #reading data that are already stored in data.json
            with open('data.json', 'r') as file:
                data = json.load(file)
        #overwriting the selected_drives in data.json with selected_items
            data["selected_drives"] = [selected_items]
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)
#Opening new window

            subprocess.Popen([sys.executable, 'idk.py'])
            Clock.schedule_once(lambda dt: self.stop(), 1)
        

if __name__ == '__main__':
    CheckboxApp().run()