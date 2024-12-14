from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import Line, Color

class PaintScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Main layout
        layout = BoxLayout(orientation="vertical")

        # Add background image
        background = Image(source="background.jpg", allow_stretch=True, keep_ratio=False)
        layout.add_widget(background)

        # Canvas for drawing
        self.painter = PaintWidget()
        layout.add_widget(self.painter)

        # Toolbar with buttons
        toolbar = BoxLayout(size_hint=(1, 0.1))
        layout.add_widget(toolbar)

        # Add buttons
        toolbar.add_widget(Button(text="Black", on_press=lambda x: self.painter.set_color((0, 0, 0, 1))))
        toolbar.add_widget(Button(text="Red", on_press=lambda x: self.painter.set_color((1, 0, 0, 1))))
        toolbar.add_widget(Button(text="Green", on_press=lambda x: self.painter.set_color((0, 1, 0, 1))))
        toolbar.add_widget(Button(text="Blue", on_press=lambda x: self.painter.set_color((0, 0, 1, 1))))
        toolbar.add_widget(Button(text="Eraser", on_press=lambda x: self.painter.toggle_eraser()))
        toolbar.add_widget(Button(text="Clear", on_press=self.clear_canvas))

        self.add_widget(layout)

    def clear_canvas(self, instance):
        """Clear the drawing canvas."""
        self.painter.canvas.clear()

class PaintWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.line_width = 2
        self.current_color = (0, 0, 0, 1)  # Default color: black
        self.eraser_mode = False  # Default mode: draw

    def on_touch_down(self, touch):
        # Set color and draw when the screen is touched
        with self.canvas:
            Color(*self.current_color)
            touch.ud["line"] = Line(points=(touch.x, touch.y), width=self.line_width)

    def on_touch_move(self, touch):
        # Add points to the line as the touch moves
        touch.ud["line"].points += [touch.x, touch.y]

    def set_color(self, color):
        """Set the color for drawing."""
        self.current_color = color
        self.eraser_mode = False  # Disable eraser mode when a new color is set

    def toggle_eraser(self):
        """Toggle eraser mode."""
        self.eraser_mode = not self.eraser_mode
        if self.eraser_mode:
            self.current_color = (1, 1, 1, 1)  # White color for erasing