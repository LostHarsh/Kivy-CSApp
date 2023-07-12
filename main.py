from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.clock import Clock
from kivy.core.window import Window
import requests

Window.size = (350, 580)


# Define the login screen
class PreSplash(Screen):
    pass


# Define the login screen
class LoginScreen(Screen):
    pass


# Define the second screen
class SecondScreen(Screen):
    pass


class RoundedGridLayout(GridLayout):
    pass


# Create the screen manager to manage different screens
class ScreenManagement(ScreenManager):
    pass


class MainApp(MDApp):

    def build(self):
        # Load the .kv file
        # kv = Builder.load_file("design.kv")
        kv = Builder.load_file("design-Final.kv")
        return kv

    def on_start(self):
        Clock.schedule_once(self.login, 2)

    def login(self, *args):
        self.root.current = "login_screen"

    def on_submit(self, username, password):
        # Check if the username and password are valid
        if username == "" and password == "":
            self.root.current = "second_screen"

    def button_click(self, Text):
        url = "http://192.168.59.2/post"
        data = {"BtnText": Text}
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print("Data sent is: " + Text)


# Run the app
if __name__ == "__main__":
    MainApp().run()
