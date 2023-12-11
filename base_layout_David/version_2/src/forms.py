from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
import platform
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.app import App
from kivymd.app import MDApp


class MainApp(MDApp):
    
    def build(self):
        Window.size = (1150, 600)
        #dark theme

        self.theme_cls.theme_style = "Light"
        #light theme
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.accent_palette = "Red"

        return Builder.load_file('../design/forms.kv')
    def login(self):
        self.root.ids.welcome_label.text = "Hello " + self.root.ids.user.text
    def clear(self):
        self.root.ids.welcome_label.text = "Welcome"
        self.root.ids.user.text = ""
        self.root.ids.password.text = ""

    #Messages control for the inputs
    def set_error_message(self, instance_textfield):
        self.screen.ids.p1.error = True
    
    def validate_textfield(self):
        text_field = self.root.ids.p1
        input_text = text_field.text.strip()

        try:
            input_value = int(input_text)  # Intentar convertir el texto a un entero
            if 3 <= input_value <= 30:
                text_field.helper_text = ""
                text_field.error = False
                text_field.text_color = 1, 1, 1, 1  # Color de texto normal
            else:
                text_field.helper_text = "Valor fuera de rango (3-30)"
                text_field.error = True
                text_field.text_color = 1, 0, 0, 1  # Rojo
        except ValueError:
            text_field.helper_text = "Ingrese un número válido"
            text_field.error = True
            text_field.text_color = 1, 0, 0, 1  # Rojo

#Colors: Red, Pink, Purple, DeepPurple,
# Indigo, Blue, LightBlue, Cyan, Teal,
# Green, LightGreen, Lime, Yellow, Amber,
# Orange, DeepOrange, Brown, Gray, BlueGray

MainApp().run()