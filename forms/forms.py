from kivy.lang import Builder
from kivymd.app import MDApp


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        #light theme
        self.theme_cls.primary_palette = "Amber"
        self.theme_cls.accent_palette = "Red"
        return Builder.load_file('forms.kv')
    def login(self):
        self.root.ids.welcome_label.text = "Hello " + self.root.ids.user.text
    def clear(self):
        self.root.ids.welcome_label.text = "Welcome"
        self.root.ids.user.text = ""
        self.root.ids.password.text = ""


#Colors: Red, Pink, Purple, DeepPurple,
# Indigo, Blue, LightBlue, Cyan, Teal,
# Green, LightGreen, Lime, Yellow, Amber,
# Orange, DeepOrange, Brown, Gray, BlueGray

MainApp().run()