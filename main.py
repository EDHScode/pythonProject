from kivy.app import App
from kivy.uix.widget import Widget

class MyApp(App):
    def build(self):
        return Widget()

if __name__ == "__main__":
    app = MyApp()
    app.run()
