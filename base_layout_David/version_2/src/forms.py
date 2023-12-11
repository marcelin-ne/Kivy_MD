#Import libraries for the design 
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
#Import packages for the logic
from calculator import Rankine_P_Close


class MainApp(MDApp):
    
    def build(self):
        Window.size = (1150, 600)
        #Theme
        self.theme_cls.theme_style = "Light"
        #Colors
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.accent_palette = "Red"
        return Builder.load_file('../design/forms.kv')
    

    def validate_textfield(self, text_field, min_limit, max_limit):
        input_text = text_field.text.strip()
        try:
            input_value = int(input_text)  # Intentar convertir el texto a un entero
            if min_limit <= input_value <= max_limit:
                text_field.helper_text = ""
                text_field.error = False
                text_field.text_color = 1, 1, 1, 1  # Color de texto normal
                return True
            else:
                text_field.helper_text = f"Valor fuera de rango ({min_limit}-{max_limit})"
                text_field.error = True
                text_field.text_color = 1, 0, 0, 1  # Rojo
                return False
        except ValueError:
            text_field.helper_text = "Ingrese un número válido"
            text_field.error = True
            text_field.text_color = 1, 0, 0, 1  # Rojo

    #Function to validate every textfield that returns true if all the textfields are correct
    def validate_all_textfields(self):
        #Validate the textfields
        if self.validate_textfield(self.root.ids.p1, 3, 30) and self.validate_textfield(self.root.ids.p2, 2000, 36000) and self.validate_textfield(self.root.ids.p3, 1000, 22000) and self.validate_textfield(self.root.ids.T6, 200, 800) and self.validate_textfield(self.root.ids.mp, 0.2, 1) and self.validate_textfield(self.root.ids.nb, 0.2, 1) and self.validate_textfield(self.root.ids.nt, 0.2, 1):
            return True
        else:
            return False

MainApp().run()