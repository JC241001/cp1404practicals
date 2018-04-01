"""
CP1404 Practicals
Dynamically create labels based on content of list
Gerard Djian
Modified from dynamic_widgets.py, 1/04/2018
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicWidgetsApp(App):
    """Main program - Kivy app to demo dynamic widget creation."""

    def __init__(self, **kwargs):
        """
        Construct main app.
        """
        super().__init__(**kwargs)
        self.name_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

    def build(self):
        """
        Build the Kivy GUI.
        :return: reference to the root Kivy widget
        """
        self.title = "Dynamic Name List"
        self.root = Builder.load_file('dynamic_kivy_list.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """
        Create labels from list entries and add them to the GUI
        :return: None
        """
        for name in self.name_list:
            # create a label for each name_list entry, specifying the text and id
            temp_label = Label(text=name, id=name)
            # add the labels to the "entries_box" using add_widget()
            self.root.ids.entries_box.add_widget(temp_label)

DynamicWidgetsApp().run()
