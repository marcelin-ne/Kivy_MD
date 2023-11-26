from kivy.lang import Builder
from kivymd.app import MDApp

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        #light theme
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.accent_palette = "Red"
        return Builder.load_file('theme.kv')

#Colors: Red, Pink, Purple, DeepPurple,
# Indigo, Blue, LightBlue, Cyan, Teal,
# Green, LightGreen, Lime, Yellow, Amber,
# Orange, DeepOrange, Brown, Gray, BlueGray

MainApp().run()