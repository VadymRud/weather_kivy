# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivy.uix.image import Image

from kivymd.bottomsheet import MDListBottomSheet, MDGridBottomSheet
from kivymd.button import MDIconButton
from kivymd.date_picker import MDDatePicker
from kivymd.dialog import MDDialog
from kivymd.label import MDLabel
from kivymd.list import ILeftBody, ILeftBodyTouch, IRightBodyTouch, BaseListItem
from kivymd.material_resources import DEVICE_TYPE
from kivymd.navigationdrawer import MDNavigationDrawer, NavigationDrawerHeaderBase
from kivymd.selectioncontrols import MDCheckbox
from kivymd.snackbar import Snackbar
from kivymd.theming import ThemeManager
from kivymd.time_picker import MDTimePicker
from kivy.uix.boxlayout import BoxLayout


class WeatherApp(App):
    theme_cls = ThemeManager()
    kv_directory = 'templates'
    title = 'Х*ва Погода'

    def build(self):
        self.root.ids.toolbar.title = 'Х*ве меню'
    #     root.ids.toolbar.title = 'Х*ве меню'
        #nav_dra_too
        self.root.ids.nav_dra_too.title = 'Х*ве меню'


if __name__ == '__main__':
    WeatherApp().run()
