from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.animation import Animation
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.behaviors import MagicBehavior

class MagicImage(MagicBehavior, ButtonBehavior, Image):
    def wobble_and_navigate(self, callback):
        anim = (
            Animation(scale_x=1.2, scale_y=0.8, duration=0.2) +
            Animation(scale_x=0.8, scale_y=1.2, duration=0.2) +
            Animation(scale_x=1, scale_y=1, duration=0.2)
        )
        anim.bind(on_complete=lambda instance, value: callback())
        anim.start(self)
