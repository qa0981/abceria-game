from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color, Rectangle
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.slider import Slider
from kivy.properties import ListProperty


class TracingWidget(Widget):
    line_width = NumericProperty(2)
    is_tracing_complete = NumericProperty(0)

    def on_touch_down(self, touch):
        with self.canvas:
            Color(0, 0, 1, 1)
            touch.ud["line"] = Line(points=(touch.x, touch.y), width=self.line_width)

    def on_touch_move(self, touch):
        if "line" in touch.ud:
            touch.ud["line"].points += [touch.x, touch.y]

    def check_tracing(self):
        total_points = sum(len(obj.points) for obj in self.canvas.children if isinstance(obj, Line))
        if total_points > 100:
            self.is_tracing_complete = 1
        else:
            self.is_tracing_complete = 0


class TracingScreen(Screen):
    letter_number = StringProperty("1")
    score = NumericProperty(0)
    username = StringProperty("Username")

    def on_enter(self):
        self.clear_canvas()

    def clear_canvas(self):
        self.ids.tracing_area.canvas.clear()

    def go_to_next_letter(self):
        self.ids.tracing_area.check_tracing()
        if self.ids.tracing_area.is_tracing_complete:
            self.score += 3
        else:
            self.score += 0

        next_letter = int(self.letter_number) + 1
        if next_letter > 52:
            next_letter = 1
        self.letter_number = str(next_letter)
        self.clear_canvas()

    def go_back(self):
        self.manager.current = "game"

class CustomSlider(Slider):
    knob_position = ListProperty([0, 0])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(value=self.update_knob_position)

    def update_knob_position(self, *args):
        x = self.x + self.value_normalized * self.width
        y = self.center_y
        self.knob_position = [x, y]