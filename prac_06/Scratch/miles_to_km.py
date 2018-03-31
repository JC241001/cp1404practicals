"""
CP1404 Practical
Kivy GUI program to convert miles to km
Gerard Djian
Started 31 March 2018
"""


from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
# from kivy.app import StringProperty


MILES_TO_KM_CONVERSION_RATE = 1.60934


class MilesToKmApp(App):
    """MilesToKmApp is a Kivy App for converting miles to km"""

    def build(self):
        """build the Kivy app from the kv file"""
        Window.size = (600, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('miles_to_km.kv')
        return self.root

    def handle_increment(self, value):
        new_value = self.valid_input() + value
        self.root.ids.input_number.text = str(new_value)
        self.convert_miles_to_km()

    def convert_miles_to_km(self):
        miles = self.valid_input()
        km = miles * MILES_TO_KM_CONVERSION_RATE
        self.root.ids.output_label.text = str(km)

    def valid_input(self):
        try:
            result = int(self.root.ids.input_number.text)
            if result < 0:
                raise ValueError
        except ValueError:
            result = 0
            self.root.ids.input_number.text = str(0.0)

        return result


MilesToKmApp().run()
