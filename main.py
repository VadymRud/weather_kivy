from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.text import LabelBase


class AddLocationForm(BoxLayout):
    def current_location_click(self):
        self.ids.notifications.text = 'click'



class WeatherApp(App):
    kv_directory = 'templates'



if __name__ == '__main__':
    WeatherApp().run()


