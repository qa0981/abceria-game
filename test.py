from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import StringProperty

class LevelSelectionScreen(Screen):
    coin_count = StringProperty("100")
    username = StringProperty("Player")

    def select_level(self, level):
        print(f"Level {level} selected!")
        # Add logic to transition to the selected level's screen

class MainApp(App):
    def build(self):
        sm = ScreenManager()

        # Adding LevelSelectionScreen to ScreenManager
        level_selection_screen = LevelSelectionScreen(name="level_selection")
        sm.add_widget(level_selection_screen)

        return sm

if __name__ == "__main__":
    MainApp().run()