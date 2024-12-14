from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Line, Rectangle

class SketchedTextInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            # Background color
            Color(1, 1, 1, 1)  # White
            self.rect = Rectangle(size=self.size, pos=self.pos)

            # Border color
            Color(0, 0, 0, 1)  # Black
            self.border = Line(width=2)

        # Bind the `update_canvas` method to size and position changes
        self.bind(size=self.update_canvas, pos=self.update_canvas)

    def update_canvas(self, *args):
        """Update the canvas when the widget's size or position changes."""
        # Update the rectangle and border
        self.rect.size = self.size
        self.rect.pos = self.pos
        self.border.rectangle = (self.x, self.y, self.width, self.height)