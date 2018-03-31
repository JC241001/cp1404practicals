"""
CP1404 Practical
Kivy GUI program to convert miles to km
Gerard Djian
Started 31 March 2018
"""


from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


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
        new_value = int(self.root.ids.input_number.text) + value
        self.root.ids.input_number.text = str(new_value)
        #self.convert_miles_to_km()

    def convert_miles_to_km(self):
            try:
                miles = int(self.root.ids.input_number.text)
                if miles < 0:
                    raise ValueError
                km = miles*MILES_TO_KM_CONVERSION_RATE
                self.root.ids.output_label.text = str(km)
            except ValueError:
                self.root.ids.output_label.text = str(0.0)


MilesToKmApp().run()
