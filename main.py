from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class MortgageCalculatorApp(MDApp):
    def build(self):
        return MDLabel(text="Hello, MortgageCalculator", halign="center")

MortgageCalculatorApp().run()