from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color


class TracingWidget(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            Color(0, 0, 1, 1)
            touch.ud["line"] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        if "line" in touch.ud:
            touch.ud["line"].points += [touch.x, touch.y]


class TracingScreen(Screen):
    def clear_canvas(self):
        self.ids.tracing_area.canvas.clear()