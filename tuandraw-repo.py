import os
import sys

# Tắt cấu hình mặc định của Kivy và chuyển thư mục làm việc
os.environ['KIVY_NO_CONFIG'] = '1'
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.utils import platform

# Cấu hình kích thước màn hình nếu chạy trên máy tính
if platform not in ('android', 'ios'):
    Window.size = (400, 650)

class MainScreen(Screen):
    pass

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        return sm

if __name__ == '__main__':
    MyApp().run()
    
