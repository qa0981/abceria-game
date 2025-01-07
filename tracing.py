from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget
from kivy.graphics import Line, Color, Rectangle
from kivy.properties import NumericProperty


class TracingWidget(Widget):
    line_width = NumericProperty(2)

    def on_touch_down(self, touch):
        with self.canvas:
            Color(0, 0, 1, 1)  # Blue color
            touch.ud["line"] = Line(points=(touch.x, touch.y), width=self.line_width)

    def on_touch_move(self, touch):
        if "line" in touch.ud:
            touch.ud["line"].points += [touch.x, touch.y]


class TracingScreen(Screen):
    letter = ""

    def set_letter(self, letter):
        self.letter = letter
        self.ids.tracing_area.canvas.clear()  # Clear any previous lines
        
        # Load the image for the current letter
        image_path = f"image/huruf/huruf_polos/letter_{self.letter}.png"
        try:
            with self.ids.tracing_area.canvas:
                Color(1, 1, 1, 1)  # White color for background
                self.ids.tracing_area.canvas.add(Rectangle(source=image_path, size=self.size, pos=self.pos))
        except Exception as e:
            print(f"Error loading image: {e}")

    def go_to_next_letter(self):
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        current_index = letters.index(self.letter)
        next_letter = letters[(current_index + 1) % len(letters)]
        self.manager.get_screen(next_letter).set_letter(next_letter)
        self.manager.current = next_letter

    def clear_canvas(self):
        self.ids.tracing_area.canvas.clear()

    def go_back(self, instance=None):
        self.manager.current = "game"