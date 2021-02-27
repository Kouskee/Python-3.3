
import kivy
from kivy.uix.codeinput import CodeInput
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        bl = BoxLayout(orientation = 'vertical', padding=[250])
        
        
        bl.add_widget(Button(text="i want", width=20, height=40, background_color = 'red'))

        bl.add_widget(Button(text="pizza", width=60, height=40, background_color = 'blue'))

        
        return bl

 
if __name__ == '__main__':
    MyApp().run()