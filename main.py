from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.text import LabelBase


class AddLocationForm(BoxLayout):


    def current_location_click(self):
        self.ids.notifications.text = 'click'
        self.ids.act_prev.title = 'фівфів'


class WeatherApp(App):
    kv_directory = 'templates'
    title = 'Х*ва Погода'
    def build(self):
        root = AddLocationForm()
        root.ids.act_prev.title = 'Х*ве меню'
        return root



if __name__ == '__main__':
    WeatherApp().run()


