from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import *

def rgb(r, g, b, a=1):
    return r / 255, g / 255, b / 255, a

class StartScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        with self.canvas.before:
            self.bg_image = Rectangle(
                source="image/bg.png",
                size=self.size,
                pos=self.pos
            )
        self.bind(size=self.update_bg, pos=self.update_bg)

        layout = BoxLayout(orientation="vertical", spacing=20, padding=[50, 100, 50, 100])

        title_label = Label(
            text="Welcome to the Drawing App",
            font_size="40sp",
            font_name="fonts/SplashBakery.otf",
            color=rgb(48, 68, 99),
            size_hint=(1, None),
            height=100
        )

        self.start_image = Image(
            source="image/playy.png",
            allow_stretch=True,
            size_hint=(None, None),
            size=(300, 250),
            pos_hint={"center_x": 0.5, "y": 0.2}
        )

        self.start_image.bind(on_touch_down=self.on_image_click)

        layout.add_widget(title_label)
        layout.add_widget(self.start_image)

        self.add_widget(layout)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

    def update_bg(self, *args):
        self.bg_image.size = self.size
        self.bg_image.pos = self.pos

    def on_image_click(self, instance, touch):
        if self.start_image.collide_point(touch.x, touch.y):
            print("Gambar diklik!")
            self.start_app()

    def start_app(self):
        self.manager.current = "paint"