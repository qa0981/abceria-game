from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color, Rectangle
from kivy.properties import NumericProperty, StringProperty
from kivy.core.window import Window


class TracingWidget(Widget):
    line_width = NumericProperty(2)

    def on_touch_down(self, touch):
        with self.canvas:
            Color(0, 0, 1, 1)
            touch.ud["line"] = Line(points=(touch.x, touch.y), width=self.line_width)

    def on_touch_move(self, touch):
        if "line" in touch.ud:
            touch.ud["line"].points += [touch.x, touch.y]


class TracingScreen(Screen):
    letter_number = StringProperty("1")

    def on_enter(self):
        self.ids.tracing_area.canvas.clear()
        self.ids.label.font_size = Window.width * 0.1

    def go_to_next_letter(self):
        next_letter = int(self.letter_number) + 1
        if next_letter > 52:
            next_letter = 1
        self.letter_number = str(next_letter)
        self.manager.current = f"tracing_{next_letter}"

    def clear_canvas(self):
        self.ids.tracing_area.canvas.clear()

    def go_back(self, instance=None):
        self.manager.current = "game"